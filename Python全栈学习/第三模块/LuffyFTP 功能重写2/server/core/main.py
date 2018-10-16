#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/22 9:50

from socket import *
import pickle
import hashlib
import os
# import configparser
from conf import settings
from threading import currentThread
from concurrent.futures import ThreadPoolExecutor #导入线程池模块
from queue import  Queue

class FTPServer(object):
    def __init__(self, management_instance):
        self.management_instance = management_instance
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((settings.HOST, settings.PORT))
        self.socket.listen(settings.MAX_CLIENT_COUNT)
        self.q = Queue(settings.MAX_CLIENT_COUNT)
        self.login_user_list = {} # {'caideyang': {'current_path': 'uploads/caideyang', 'conn': self.conn } }
        self.status_dic = {
            200: "Successful !",
            201: "File md5 the same as client",
            202: "File md5 not the same as client",
            300: "File is ready to send !",
            301: "File is read to recieve !",
            400: "Failed !",
            401: "Action not exist !",
            402: "Parameters wrong !",
            403: "Path not exist !",
            404: "File not exist!",
            405: "Path name already exists !",
            406: "No enough space to save file !",
        }

    def run_forever(self):
        print("Starting server on %s:%s" % (settings.HOST, settings.PORT))
        while True:
            conn, client_addr = self.socket.accept()
            # t = Thread(target=self.task, args=(conn, client_addr))
            self.pool = ThreadPoolExecutor(settings.MAX_CLIENT_COUNT) #  settings.MAX_CLIENT_COUNT  5
            self.pool.submit(self.task, conn, client_addr)
            self.q.put(conn)
            # print("Ftp Client %s is  connecting...." % str(self.client_addr))
            # request_data = self.recv_data()
            # auth_result = self._auth(request_data)
            # if auth_result == 200:  # 如果认证通过
            #     self.handle()
            # else:
            #     self.conn.close()

    def task(self, conn, client_addr):
        while True:
            try:
                print(currentThread())
                print("Ftp Client %s is  connecting...." % str(client_addr))
                request_data = self.recv_data(conn)
                if not request_data: break
                auth_result = self._auth(conn, request_data)
                if auth_result == 200:  # 如果认证通过
                    self.handle(conn)
                else:
                    conn.close()
            except Exception as e:
                print(e)
                self.q.get(conn)
                print(client_addr, "断开连接")
                break

    # def stop(self):
    #     self.socket.close()
    #     del self.socket
    #
    # def restart(self):
    #     self.stop()
    #     self.run_forever()


    def parser_account(self,):
        pass

    def get_md5(self, data, type="str"):
        m = hashlib.md5()
        if type == "str":
            m.update(data.encode('utf-8'))
        elif type == "file":
            if not os.path.isfile(data):
                return None
            with open(data, 'rb') as f:
                for line in f:
                    m.update(line)
        else:
            exit("Type error !")
        return m.hexdigest()

    def get_info(self, name):
        user_file = os.path.join(settings.db, name)
        with open(user_file, 'rb') as user_obj:
            user_info = pickle.load(user_obj)
        return user_info

    def save_info(self, user_info, name):
        user_file = os.path.join(settings.db, name)
        with open(user_file, 'wb') as user_obj:
            pickle.dump(user_info, user_obj)

    def send_data(self, conn, **kwargs):
        data = {}
        data.update(kwargs)
        pickle_data = pickle.dumps(data)
        conn.send(pickle_data)

    def recv_data(self, conn):
        data = conn.recv(settings.MAX_RECV_BYTE)
        if not data:
            return False
        return pickle.loads(data)

    def recv_byte_data(self, conn, to_trans_size, filename=None, mode=None, file_md5=None, type='msg'):
        if type == 'msg': #传输的是要打印的
            msg = b''
            recv_size = 0
            while recv_size < to_trans_size:
                data = conn.recv(settings.MAX_RECV_BYTE)
                recv_size += len(data)
                msg += data
            print(msg.decode(settings.DEFAULT_BYTE_CODE))
            return 200
        elif type=="file": # 传输的是文件
            # print("-------->开始传输！！！！")
            recv_size = 0
            with open(filename, mode) as f:
                while recv_size < to_trans_size:
                    data = conn.recv(settings.MAX_RECV_BYTE)
                    f.write(data)
                    recv_size += len(data)
            print("传输完成")
            if self.get_md5(filename, type="file") == file_md5:
                return 201
            else:
                return 202
        else:
            print("传输失败！")
            return 400

    def handle(self, conn):
        while True:

            try:
                request_data = self.recv_data(conn)
                if not request_data: break
                action = request_data['action']
                if hasattr(self, '_%s' % action):
                    func = getattr(self, '_%s' % action)
                    print(request_data)
                    func(conn, request_data)
                else:
                    request_data['status'] = 401
                    self.send_data(conn, **request_data)
            except Exception as e:
                print(e)
                self.q.get(conn)
                print(self.client_addr,"连接断开")
    def is_authorized(self, conn, request_data):
        if request_data['username'] not in self.login_user_list:
            request_data["status"] = 400
            self.send_data(**request_data)
            conn.close()
            self.q.get(conn)
            return False
        else:
            return True
    def is_path_exist(self, path):
        if os.path.isfile(path):
            pass
    def get_data_size(self, data, type='data'):
        pass

    def _auth(self, conn, request_data):
        """用户认证"""
        print(request_data)
        username = request_data['username']
        password = request_data['password']
        data_dic = {}
        action = 'auth'
        if username in os.listdir(settings.db):
            user_info = self.get_info(username)
            print(user_info.__dict__)
            if user_info.password == self.get_md5(password):
                self.login_user_list[username] = user_info
                request_data['status'] = 200
                request_data['msg'] = "认证成功！"
                request_data['current_path'] = user_info.current_path
            else:
                request_data['status'] = 400
                request_data['msg'] = "认证失败！用户名密码错误！"
                # self.conn.close()
        else:
            request_data['status'] = 400
            request_data['msg'] = "认证失败！无此用户！"
            # self.conn.close()
        request_data['username'] =  username
        print(request_data)
        self.send_data(conn, **request_data)
        return request_data['status']

    def _df(self, conn, request_data):
        if self.is_authorized(conn, request_data):
            request_data['status'] = 200
            request_data['space_info'] = self.login_user_list[request_data['username']].space_info
            self.send_data(conn, **request_data)

    def _ls(self, conn, request_data):
        print("===========>",currentThread())
        if self.is_authorized(conn, request_data):
            if len(request_data['args']) >= 2:
                dir = os.path.join(request_data['current_path'], request_data['args'][-1])
                abs_path = os.path.join(settings.BASE_DIR, request_data['current_path'], request_data['args'][-1])
            else:
                dir = request_data['current_path']
                abs_path = os.path.join(settings.BASE_DIR, request_data['current_path'])
            print(abs_path)
            if os.path.isdir(abs_path):
                request_data['status'] = 200
                file_list = os.listdir(abs_path)
                if file_list:
                    msg = "当前目录的文件情况如下:\n文件名    文件大小   创建时间            修改时间              类型：\n"
                    for file_name in file_list:
                        file = os.path.join(abs_path, file_name)
                        print(file)
                        file_size = os.path.getsize(file)
                        import time
                        create_time = time.strftime("%x %X", time.localtime(os.path.getctime(file)))
                        modify_time = time.strftime("%x %X", time.localtime(os.path.getmtime(file)))
                        file_type = "文件夹" if os.path.isdir(file) else "文件"
                        file_info = "【%s】   【%s】   【%s】   【%s】   【%s】 \n" % (
                        file_name, file_size, create_time, modify_time, file_type)
                        print(file_info)
                        msg += file_info
                else:
                    msg = "目录%s没有文件！" % dir
                request_data['data_len'] = len(msg)
                self.send_data(conn, **request_data)  # 将数据的长度信息发送给客户端
                conn.send(msg.encode(settings.DEFAULT_BYTE_CODE))

            else:
                request_data['status'] = 403
                self.send_data(conn, **request_data)

    def _mkdir (self, conn, request_data):
        if self.is_authorized(conn, request_data):
            if len(request_data["args"]) != 2:
                request_data['status'] = 402
                # self.send_data()
            else:
                new_dir = request_data["args"][1]
                abs_path = os.path.join(settings.BASE_DIR, request_data["current_path"], new_dir)
                if os.path.exists(abs_path):
                    request_data['status'] = 405
                else:

                    os.mkdir(abs_path)
                    request_data['status'] = 200
                    request_data["msg"] = "创建目录%s成功" % new_dir
            self.send_data(conn, **request_data)

    def _cd(self, conn, request_data):
        print(request_data)
        if self.is_authorized(conn, request_data):
            username = request_data['username']
            if len(request_data["args"]) == 1:
                print("1111111111111当前路径")
                request_data['status'] = 200
                current_path = '%s/%s' %(settings.USER_BASE_DIR, username)
                request_data["msg"] = "切换成功，当前目录：%s" % current_path
            elif len(request_data["args"]) == 2:
                to_path = request_data["args"][1]
                current_path_list = request_data["current_path"].split('\\')
                if "/" in to_path:
                    new_path_list = to_path.split('/')
                    flag = True
                    while flag:
                        for path in new_path_list:
                            if path == "..":
                                tmp_path = current_path_list.pop()
                                if len(current_path_list) == 0:
                                    request_data["msg"] = "没有权限切换到对应目录"
                                    request_data['status'] = 403
                                    flag = False
                                    break
                            else:
                                current_path_list.append(path)
                        new_path = "\\".join(current_path_list)
                        break
                    if flag:
                        if os.path.isdir(os.path.join(settings.BASE_DIR, new_path)):
                            current_path = new_path
                            request_data["msg"] = "切换成功，当前目录：%s" % current_path
                            request_data['status'] = 200

                        else:
                            request_data["msg"] = "要切换的目录【%s】在当前路径不存在" % to_path
                            request_data['status'] = 403

                    else:
                        pass
                elif to_path == "..":
                    tmp_path = current_path_list.pop()
                    if len(current_path_list) == 0:
                        request_data["msg"] = "没有权限切换到对应目录"
                        request_data['status'] = 403

                    else:
                        current_path = "\\".join((current_path_list))
                        request_data["msg"] = "切换成功，当前目录：%s" % current_path
                        request_data['status'] = 200

                else:
                    current_path = os.path.join(request_data["current_path"], to_path)
                    if os.path.exists(os.path.join(settings.BASE_DIR, current_path)):
                        request_data["msg"] = "切换成功，当前目录：%s" % current_path
                        request_data['status'] = 200

                    else:
                        request_data["msg"] = "要切换的目录【%s】在当前路径不存在" % to_path
                        request_data['status'] = 403
            else:
                request_data['status'] = 402
        if request_data['status'] == 200:
            self.login_user_list[username].current_path = current_path
            request_data["current_path"] = current_path
        else:
            pass
        print(request_data)
        self.send_data(conn, **request_data)

    def _put(self, conn, request_data):
        print(request_data)
        current_path = self.login_user_list[request_data['username']].current_path
        if self.is_authorized(conn, request_data):
            request_data["status"] = 200
            abs_file_name = os.path.join(settings.BASE_DIR, current_path, request_data['filename'])
            request_data["server_file_md5"] = self.get_md5(abs_file_name, type="file")
            request_data["server_file_size"] = 0
            if request_data["server_file_md5"] == request_data['md5']:
                request_data['status'] = 201
            else:
                if os.path.isfile(abs_file_name): # 有该文件
                    request_data["server_file_size"] = os.path.getsize(abs_file_name)
                    request_data['status'] = 202
            free_space = self.login_user_list[request_data['username']].space_info[2] * 1024 * 1024
            request_data['space_aviable'] = free_space + request_data["server_file_size"] - request_data["filesize"]
            if request_data['space_aviable'] < 0:
                request_data['status'] = 303
            self.send_data(conn, **request_data)
            request_data = self.recv_data(conn)
            print("111111111111->",request_data)
            request_data["status"] = self.recv_byte_data(conn, request_data["filesize"] - request_data["seek_place"],
                                filename=abs_file_name,
                                mode=request_data["mode"],
                                file_md5=request_data['md5'],
                                type="file")
            self.login_user_list[request_data["username"]].change_space_size(request_data['filesize'] - request_data["seek_place"])
            self.save_info(self.login_user_list[request_data['username']], request_data['username'])
            self.send_data(conn, **request_data)
            # exit("put退出！")

    def _get(self, conn, request_data):
        print(request_data)
        if self.is_authorized(conn, request_data):
            username = request_data['username']
            current_path = self.login_user_list[request_data['username']].current_path
            abs_file_name = os.path.join(settings.BASE_DIR, current_path, request_data['filename'])
            request_data['md5'] = self.get_md5(abs_file_name, type="file")
            if not os.path.isfile(abs_file_name):
                request_data['status'] = 404
                self.send_data(conn, **request_data)
            elif request_data["md5"] == request_data["file_md5"]:
                request_data["status"] = 201
                self.send_data(conn, **request_data)
            else:
                request_data['status'] = 200
                request_data['filesize'] = os.path.getsize(abs_file_name)

                if request_data["file_md5"]:
                    request_data["status"] = 202
                self.send_data(conn, **request_data)
                request_data = self.recv_data(conn)
                print(request_data)
                seek_place = request_data["seek_place"]
                with open(abs_file_name, 'rb') as f:
                    f.seek(seek_place)
                    for line in f:
                        conn.send(line)
                print("传输完成")

            # exit("get方法退出")

    def _logout(self, conn, request_data):
        self.save_info(self.login_user_list[request_data['username']], request_data['username'])
        self.login_user_list.pop(request_data["username"])
        self.q.get(conn)
        # self.conn.close()


if __name__ == "__main__":
    pass