#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 13:49

import time
import pickle
import hashlib
import optparse
import os
from socket import *
from conf import settings



#定义一个进度条
import sys


def process_bar(num, total):
    rate = float(num) / total
    ratenum = int(rate * 100)
    r = '\r[{}{}]已传输完成{}，{}%'.format('*' * ratenum + ">", ' ' * (100 - ratenum), num, ratenum)
    sys.stdout.write(r)
    sys.stdout.flush()


class FTPClient():
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="ftp server ip_addr")
        parser.add_option("-P", "--prot", type="int", dest="port", help="ftp server port")
        self.options, self.args = parser.parse_args()
        print(self.options, self.args)
        self.username = None
        self.current_path = None
        self.is_certified = False # 默认是未认证的
        self.menu = """
                   pwd. 查看当前目录
                   df. 查看目录可用空间
                   ls. 查看当前目录文件
                   mkdir. 创建目录
                   cd . 切换目录
                   put. 文件上传
                   get. 文件下载
                   logout. 断开连接
               """
        # self.menu_dict = {
        #     "pwd": self.pwd,
        #     "df": self.df,
        #     "ls": self.pwd,
        #     "mkdir": self.pwd,
        #     "cd": self.pwd,
        #     "put": self.put,
        #     "get": self.get,
        #     "logout": self.logout
        # }

        self.client = socket(AF_INET, SOCK_STREAM)
        self.verify_data()
        self.interactive()

    def verify_data(self):
        """查看传入的参数是否正确"""
        if not self.options.server or not self.options.port:
            self.useage()
            exit("Invalid options...")
    def useage(self):
        print("Usage: python ftp_client.py  -s <server_ip>  -P <port_number>")

    def send_data(self, **kwargs):
        data = {}
        data.update(kwargs)
        pickle_data = pickle.dumps(data)
        self.client.send(pickle_data)

    def recv_data(self):
        data = self.client.recv(settings.MAX_RECV_BYTE)
        return pickle.loads(data)

    def recv_byte_data(self, to_trans_size, filename=None, mode=None, file_md5=None, total_size=None, type='msg'):
        if type == 'msg': #传输的是要打印的
            msg = b''
            recv_size = 0
            while recv_size < to_trans_size:
                data = self.client.recv(settings.MAX_RECV_BYTE)
                recv_size += len(data)
                msg += data
            print(msg.decode(settings.DEFAULT_BYTE_CODE))
            return 200
        elif type=="file": # 传输的是文件
            # print("-------->开始传输！！！！")
            recv_size = 0
            with open(filename, mode) as f:
                while recv_size < to_trans_size:
                    data = self.client.recv(settings.MAX_RECV_BYTE)
                    f.write(data)
                    recv_size += len(data)
                    self.process_bar(recv_size, total_size)
            print("传输完成")
            if self.get_md5(filename, type="file") == file_md5:
                return 201
            else:
                return 202
        else:
            print("传输失败！")
            return 400


    def get_md5(self,data, type="str"):
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

    def process_bar(self, num, total):
        rate = float(num) / total
        ratenum = int(rate * 100)
        r = '\r[{}{}]已传输完成{}，{}%'.format('*' * ratenum + ">", ' ' * (100 - ratenum), num, ratenum)
        sys.stdout.write(r)
        sys.stdout.flush()

    def interactive(self):
        try:
            print("正在试图连接FTP服务器。。。")
            self.client.connect((self.options.server, self.options.port))
            self._auth()
            while self.is_certified:
                print(self.menu)
                commands = input("%s@%s>>" % (self.username, self.current_path)).strip()
                if not commands: continue
                request_dic ={}
                request_dic['username'] = self.username
                request_dic['current_path'] = self.current_path
                request_dic['action'] = commands.split()[0]
                request_dic['args'] = commands.split()

                if hasattr(self, "_%s" % commands.split()[0]):
                    func = getattr(self, '_%s' % commands.split()[0])
                    func(request_dic)
                else:
                    print("输入有误！")
            else:
                print("当前用户未认证！！！")
        except Exception as e:
            print(e)
            # self.client.close()

    def _auth(self):

        username = input("请输入您的账号: ").strip()
        password = input("请输入您的密码：").strip()
        data = {
            "action": "login",
            "username" : username,
            "password": password
        }
        self.send_data(**data)
        recvd_data = self.recv_data()
        if recvd_data['status'] == 200:
            self.is_certified = True
            self.username = username
            self.current_path = recvd_data['current_path']
        else:
            self.is_certified = False
        print(recvd_data['msg'])



    def _pwd(self, request_dic):
        print("当前路径: 【%s】" % self.current_path)
        # recvd_data = self.client.recv(8192)
        # print(recvd_data.decode('utf-8'))

    def _df(self, request_dic):
        self.send_data(**request_dic)
        recv_data = self.recv_data()
        # print(recv_data)
        if recv_data['status'] == 200:
            print("空间限额：【%s】MB  已使用空间：【%s】MB 剩余空间: 【%s】 MB" %(recv_data['space_info'][0], recv_data['space_info'][1], recv_data['space_info'][2]))
        else:
            print("获取空间信息失败！")


    def _ls(self, request_dic):
        self.send_data(**request_dic)
        recv_data = self.recv_data()
        print(recv_data)
        if recv_data['status'] == 200:
            msg_size = recv_data['data_len']
            self.recv_byte_data(msg_size)
        else:
            print(recv_data['status'])

    def _mkdir(self, request_dic):
        self.send_data(**request_dic)
        recv_data = self.recv_data()
        if recv_data['status'] == 200:
            print(recv_data['msg'])
        else:
            print(recv_data['status'])

    def _cd(self, request_dic):
        self.send_data(**request_dic)
        recv_data = self.recv_data()
        if recv_data['status'] == 200:
            self.current_path = recv_data["current_path"]
            print(recv_data['msg'])
        else:
            print(recv_data['status'])


    def _put(self, request_dic):
        """
        1.判断本地文件是否存在，存在则把本地文件相关信息发给服务器端，等待服务器响应
        send {"filename":"1.jpg", "filesize":123456, "file_md5":"abcdefg",'status':True }
        3. 根据服务端响应做出相应的操作
        3.1 如果服务器不存在该文件，则直接上传，如果存在且Md5相同，则不上传，如果存在，且md5不相同，则上传
        3.2 用户选择是否覆盖还是重传
        3.3 提交客户端端响应数据
        send {"filename":"1.jpg","filesize":123456, "file_md5":"abcdefg","seek_palce":1112,  }
        5. 开始发送数据，当文件传输完毕时关闭文件，等待服务端返回上传的结果
        7.获取md5结果，结束上传
        """
        # self.send_data(**request_dic)
        print(request_dic)
        print(request_dic)
        if len(request_dic["args"]) != 2 :
            print("参数错误！")
        else:
            request_dic["filename"]= request_dic["args"][1]
            abs_file_path = os.path.join(settings.upload_path, request_dic["filename"])
            request_dic["md5"] = self.get_md5(abs_file_path, type='file')
            if request_dic["md5"]: # 文件存在
                request_dic["filesize"] = os.path.getsize(abs_file_path)
                # send_msg = {"filename":filename, "filesize":filesize, "file_md5": file_md5,"status": True}
                print(request_dic)
                self.send_data(**request_dic) # 将要上传文件信息发送给服务端
                recvd_data = self.recv_data() # 3. 根据服务端响应做出相应的操作
                print(recvd_data)
                # if recvd_data['server_file_md5'] == request_dic["md5"]:
                if recvd_data["status"] == 201:
                    print("对应文件已经存在，且内容一致！！！！")
                    # seek_place = -1
                    # print(22222222222222)
                    # msg = self.client.recv(8192)
                    # print(msg)
                # elif recvd_data['space_aviable'] <= 0 :
                elif recvd_data["status"] == 303:
                    print("服务器可用空间不足！")
                else:
                    if recvd_data["status"] == 202: # 服务器有该文件，但内容不全
                        print(recvd_data)
                        # seek_place = recvd_data['server_file_size']

                        choice = input("是否覆盖？1-覆盖，0-续传").strip()
                        if choice == '1':
                            seek_place = 0
                            request_dic['mode'] = 'wb'
                        else:
                            seek_place = recvd_data['server_file_size']
                            request_dic['mode'] = 'ab'
                    else: #服务器无该文件
                        seek_place = 0
                        request_dic['mode'] = 'wb'
                    request_dic['seek_place'] = seek_place
                    self.send_data(**request_dic) # 3.3 提交客户端端响应数据
                    # self.client.send(pickle.dumps(send_msg))
                    to_send_size = request_dic["filesize"] - request_dic['seek_place']  # 需要发送的字节数
                    with open(abs_file_path, 'rb') as f:
                        f.seek(seek_place)
                        while seek_place < request_dic["filesize"] :
                            data = f.readline()
                            self.client.send(data)
                            seek_place += len(data)
                            # print(seek_place)
                            self.process_bar(seek_place, request_dic["filesize"])
                    print("传输完成！")
                    recvd_data = self.recv_data()  # 7. 获取服务端返回的传输状态
                    if recvd_data['status'] == 201:
                        print("传输成功，md5校验通过！")
                    elif recvd_data['status'] == 202:
                        print("传输成功，md5校验失败！")
                    else:
                        print("传输失败！")
            else:
                print("本地文件不存在！")

    def _get(self, request_dic):
        request_dic["filename"] = request_dic["args"][-1]
        abs_file_path = os.path.join(settings.BaseDir,settings.download_path, request_dic["filename"])
        request_dic["file_md5"] = self.get_md5(abs_file_path, type='file')
        request_dic["local_file_size"] = 0
        if os.path.isfile(abs_file_path):
            request_dic["local_file_size"] = os.path.getsize(abs_file_path)
        self.send_data(**request_dic)
        recvd_data = self.recv_data()

        if recvd_data['status'] == 404:
            print("服务器文件不存在")
        elif recvd_data['status'] == 201:
            print("服务器文件和本地文件md5相同！")
        else:
            # 可以开始正常传输,判断本地是否有该文件
            if recvd_data['status'] == 202:
                choice = input("是否覆盖？1-覆盖，0-续传").strip()
                if choice == '1':
                    mode = 'wb'
                    recvd_data['seek_place'] = 0
                else:
                    recvd_data['seek_place'] = recvd_data["local_file_size"]
                    mod = 'ab'
            else:
                mode = 'wb'
                recvd_data['seek_place'] = 0
            # print("----->",recvd_data)
            self.send_data(**recvd_data)
            to_recv_size = recvd_data["filesize"] - recvd_data['seek_place']

            status = self.recv_byte_data(to_recv_size,
                                filename=abs_file_path,
                                mode=mode,
                                file_md5=recvd_data["md5"],
                                total_size = recvd_data["filesize"],
                                type="file")
            if status == 201:
                print("下载成功，新文件和源文件md5校验一直！")
            elif status == 202:
                print("下载成功，新文件和源文件md5校验不一致！")
            else:
                print("下载失败！")

    def _logout(self, request_dic):
        self.send_data(**request_dic)
        self.client.close()
        exit("退出")

if __name__ =="__main__":
    FTPClient()
    # print(Client().menu)