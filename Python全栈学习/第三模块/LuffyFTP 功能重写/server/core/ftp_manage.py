#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 7:36

import os
import time
import pickle
import hashlib
from conf import settings


def get_md5(data, type="str"):
    m = hashlib.md5()
    if type == "str":
        m.update(data.encode('utf-8'))
    elif type == "file":
        if not os.path.isfile(data):
            return None
        with open(data,'rb') as f:
            for line in f:
                m.update(line)
    else:
        exit("Type error !")
    return m.hexdigest()

def get_info(name):
    user_file = os.path.join(settings.db, name)
    with open(user_file, 'rb') as user_obj:
        user_info = pickle.load(user_obj)
    return user_info

def save_info(user_info, name):
    user_file = os.path.join(settings.db, name)
    with open(user_file, 'wb') as user_obj:
        pickle.dump(user_info, user_obj)
        # pickle.dump()

class FtpManage():
    def __init__(self, conn):
        # 读取数据库
        # self.name = None
        self.conn = conn
        self.is_certified  = False  # 是否已经认证
        self.current_path = None    # 当前路径
        # self.db_file = os.path.join(settings.db, name)
        self.db_file = None
        self.user_info = None

    # 用户登陆
    def login(self, request):
        request = eval(request)
        self.name = request['name']
        password = request['password']
        send_data = {}
        send_data['action'] = 'login'
        send_data['response'] = {}
        if self.name in os.listdir(settings.db):
            self.user_info = get_info(self.name)
            # print(self.user_info.__dict__)
            if self.user_info.password == password:
                self.is_certified = True
                self.current_path = self.user_info.current_path
                send_data['response']['msg'] = "认证成功！"
            else:
                send_data['response']['msg'] = "认证失败！用户名密码错误！"
        else:
            send_data['response']['msg'] = "认证失败！无此用户！"
        send_data['is_certified'] = self.is_certified
        # print(send_data)
        # self.conn.send(pickle.dumps(send_data))
        return pickle.dumps(send_data)
    def pwd(self, request):
        # print(request)
        msg = "当前路径：%s" % self.current_path
        # self.conn.send(msg.encode('utf-8'))
        return msg.encode('utf-8')

    def mkdir(self, request):
        # print(request)
        new_dir = request.split()[1]
        abs_path = os.path.join(settings.BaseDir, self.current_path)
        if new_dir in os.listdir(abs_path):
            msg = "该目录名已经被占用！"
        else:
            os.makedirs(os.path.join(abs_path, new_dir))
            msg = "目录【%s】创建成功" % new_dir
        # self.conn.send(msg.encode('utf-8'))
        return msg.encode('utf-8')

    def df(self, request):
        # print(self.user_info.__dict__)
        space_info = self.user_info.space_info
        print(space_info)
        print("空间限额：【%s】MB  已使用空间：【%s】MB  剩余空间: 【%s】 MB" %(space_info[0], space_info[1], space_info[2]))
        msg = {}
        msg['quota'] = space_info[0]
        msg['used_space'] = space_info[1]
        msg['aviable_space'] = space_info[2]

        return pickle.dumps(msg)

    # 切换目录
    def cd(self, request):
        print(request)
        if request == "cd":
            self.current_path = '%s/%s' %(settings.Ftp_Base_Dir, self.name)
            msg = "切换成功，当前目录：%s" % self.current_path
        else:
            to_path = request.split()[1]
            current_path_list = self.current_path.split('\\')
            if '/' in to_path:
                new_path_list = to_path.split('/')
                # print(new_path_list)
                flag = True
                while flag:
                    for path in new_path_list:
                        if path == '..':
                            tmp_path = current_path_list.pop()
                            # print(tmp_path)
                            # print(self.name)
                            if len(current_path_list) == 0:
                                msg = "没有权限切换到对应目录！"
                                flag = False
                                break
                        else:
                            current_path_list.append(path)
                    new_path = "\\".join(current_path_list)
                    break
                if flag == True:
                    if os.path.isdir(os.path.join(settings.BaseDir, new_path)):
                        self.current_path = new_path
                        msg = "切换成功，当前目录：%s" % self.current_path
                    else:
                        msg = "要切换的目录【%s】在当前路径不存在" % to_path
                else:
                    pass
            elif to_path == '..':
                tmp_path = current_path_list.pop()
                # if tmp_path == self.name:
                if len(current_path_list) == 0:
                    msg = "没有权限切换到对应目录！"
                else:
                    self.current_path = "\\".join(current_path_list)
                    msg = "切换成功，当前目录：%s" % self.current_path
            else:
                abs_path = os.path.join(settings.BaseDir, self.current_path)
                # if to_path in os.listdir(abs_path):
                if os.path.isdir(os.path.join(abs_path, to_path)):
                    self.current_path = os.path.join(self.current_path, to_path)
                    msg = "切换成功，当前目录：%s" % self.current_path
                else:
                    msg = "要切换的目录【%s】在当前路径不存在" % to_path
        # self.conn.send(msg.encode('utf-8'))
        self.user_info.current_path = self.current_path
        return msg.encode('utf-8')

    # 查看目录下文件
    def ls(self, request):
        print(request)
        # print(settings.BaseDir)
        # print(self.current_path)
        abs_path = os.path.join(settings.BaseDir, self.current_path)
        # print(abs_path)
        files = os.listdir(abs_path)
        if files:
            print(files)
            msg = "当前目录的文件情况如下:\n文件名    文件大小   创建时间            修改时间              类型：\n"
            for file_name in files:
                file = os.path.join(abs_path, file_name)
                print(file)
                file_size = os.path.getsize(file)
                import time
                create_time = time.strftime("%x %X", time.localtime(os.path.getctime(file)))
                modify_time = time.strftime("%x %X", time.localtime(os.path.getmtime(file)))
                file_type = "文件夹" if os.path.isdir(file) else "文件"
                file_info = "【%s】   【%s】   【%s】   【%s】   【%s】 \n"  % (file_name, file_size, create_time, modify_time, file_type)
                print(file_info)
                msg += file_info
        else:
            msg = "当前目录没有文件！"
        print(msg)
        # send_data = {}
        # send_data['action'] = 'pwd'
        # send_data['is_certified'] = self.is_certified
        # send_data['response'] = {}
        # send_data['response']['msg'] = msg
        # print(send_data)
        # self.conn.send(pickle.dumps(send_data))
        # self.conn.send(msg.encode('utf-8'))
        return msg.encode('utf-8')

    #上传
    def put(self, request):
        """
        2.收到客户端上传文件的请求，判断该文件是否在服务器端存在，直接查看文件md5值
        2.1 如果md5值相同，则文件存在
        2.2 如果md5值不同，则告知客户端文件大小,如果md5值为None，则文件不存在
        2.3 校验服务器空间是否充足，如果不足，则在1.2中同时告知客户端文件不足的信息
        send {"filename":'1.jpg', "server_file_md5":'123333', "filesize": 1111, "space_aviable": 2334556 }
        4 服务端收到客户端数据，ruguo seek_size = -1则不上传

        4.1 如果seek_size = 0 ,则 wb 模式打开文件
        4.2 如果seek_size > 0 ,则ab 模式打开文件
        4.3 开始接收客户端数据
        6. 当数据接收完成时，返回接收到的数据md5校验结果
        """
        print(request)
        filename = request.split()[-1]
        recv_data = pickle.loads(self.conn.recv(8192))
        if recv_data['status']:
            abs_file_path = os.path.join(settings.BaseDir, self.current_path, filename)
            server_file_md5 = get_md5(abs_file_path, "file")
            if server_file_md5 == recv_data['file_md5']:
                print("服务器已经有相同文件！")
                send_msg = {"filename": filename,
                            "server_file_md5": server_file_md5 }
                self.conn.send(pickle.dumps(send_msg))
            else:
                if server_file_md5:
                    filesize = os.path.getsize(abs_file_path)
                else:
                    filesize = 0
                space_aviable = pickle.loads(self.df(""))['aviable_space'] * 1024 * 1024 + filesize - recv_data['filesize']
                send_msg = {"filename": filename,
                            "server_file_md5": server_file_md5,
                            "filesize": filesize,
                            "space_aviable": space_aviable }
                self.conn.send(pickle.dumps(send_msg))
                if space_aviable <= 0:
                    print("服务器空间不够")
                else: #等待客户端响应
                    recv_data = pickle.loads(self.conn.recv(8192))
                    # print(recv_data)
                    if recv_data['seek_size'] == 0:
                        f = open(abs_file_path, 'wb')
                    else:
                        f = open(abs_file_path, 'ab')
                    # 开始接收数据
                    flag = True
                    while flag:
                        data = self.conn.recv(8192)
                        # print(data)
                        time.sleep(0.000001)
                        f.write(data)
                        if len(data)< 8192:
                            flag = False
                    f.close()
                    server_file_md5 = get_md5(abs_file_path, "file")
                    if recv_data['file_md5'] == server_file_md5:
                        print("传输完成，md5校验通过！")
                        send_msg['status'] = 1
                    else:
                        print("传输完成，md5校验失败！")
                        send_msg['status'] = 0
                    self.user_info.change_space_size(recv_data['filesize'] - filesize)
                    save_info(self.user_info, self.name )

                self.conn.send(pickle.dumps(send_msg))
        else: # 客户端没有对应的文件，则不做任何操作
            pass
        msg = ''
        return msg.encode('utf-8')

    #下载
    def get(self, request):
        # print(request)
        filename = request.split()[-1]
        abs_file = os.path.join(settings.BaseDir, self.current_path, filename)
        if os.path.isfile(abs_file):
            file_md5 = get_md5(abs_file, type='file')
            file_size = os.path.getsize(abs_file)
            # 判断文件是否存在
            res = {"status":1, "msg":"准备就绪", "md5":file_md5, "file_size": file_size }
            self.conn.send(pickle.dumps(res))
            # 接收客户端开始传输的指令
            res2 = pickle.loads(self.conn.recv(8192))
            # print(res2)
            seek_place = res2['seek_place']  # 获取客户端让开始传输的位置
            to_send_size = file_size - seek_place  #需要发送的字节数
            # print(to_send_size)
            with open(abs_file,'rb') as f:
                f.seek(seek_place)
                while to_send_size > 0:
                    self.conn.send(f.read(8192))
                    time.sleep(0.000001)
                    to_send_size -= 8192

        else:
            return pickle.dumps({"status":-1,"msg":"文件不存在"})


        msg = ''
        return msg.encode('utf-8')

    def logout(self,request):
        # print(self.current_path)
        save_info(self.user_info, self.name)
        msg = ''
        return msg.encode('utf-8')

if __name__ == "__main__":
    pass