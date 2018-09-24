#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 13:49

import socket
import pickle
import hashlib
import os
from conf import settings

def get_md5(data, type="str"):
    m = hashlib.md5()
    if type == "str":
        m.update(data.encode('utf-8'))
    elif type == "file":
        with open(data,'rb') as f:
            for line in f:
                m.update(line)
    else:
        exit("Type error !")
    return m.hexdigest()

class login_required():
    pass

class Client():
    def __init__(self):
        self.is_certified = False # 默认是未认证的
        self.menu = """
                   pwd. 查看当前目录
                   df. 查看目录可用空间
                   ls. 查看当前目录文件
                   mkdir. 创建目录
                   cd . 切换目录
                   put. 文件上传
                   get. 文件下载
                   exit. 断开连接
               """
        self.menu_dict = {
            "pwd": self.pwd,
            "df": self.pwd,
            "ls": self.pwd,
            "mkdir": self.pwd,
            "cd": self.pwd,
            "put": self.put,
            "get": self.get,
            "exit": self.logout
        }
        self.manage()

    def manage(self):
        self.client = socket.socket()
        print("...............")
        try:
            print("正在试图连接FTP服务器。。。")
            self.client.connect(('localhost',8888))
            self.login()
            while self.is_certified:
                print(self.menu)
                commands = input("请输入你的命令：").strip()
                command = commands.split()[0]
                argvs = commands[1:]
                if command in self.menu_dict:
                    self.menu_dict[command](argvs)
                else:
                    print("输入有误！")
        except OSError as e:
            print(e)
            # self.client.close()

    def login(self):

        request = {}
        while True:
            request['name'] = input("请输入您的账号: ").strip()
            password = input("请输入您的密码：").strip()
            request['password'] = get_md5(password)
            data = {
                "action": "login",
                "request" : "%s" % request
            }
            self.client.send(pickle.dumps(data))
            recv_data = self.client.recv(8192)
            recv_data = pickle.loads(recv_data)
            # print(type(recv_data))
            self.is_certified = recv_data['is_certified']
            if self.is_certified:
                print("FTP服务器认证通过，登陆成功！")
                self.name = request['name']
                while True:
                    print(self.menu)
                    messages = input("请输入您要执行的命令：").strip()
                    args = messages.split()
                    choice = args[0]
                    if choice in self.menu_dict:
                        req_data = {}
                        req_data['action'] = choice
                        req_data['request'] = messages
                        self.client.send(pickle.dumps(req_data))
                        self.menu_dict[choice](args)
                    else:
                        print("未知选项，请重试！")

            else:
                print("账号密码认证失败！")

    def logout(self,args):
        pass


    def pwd(self, args):
        # print(args)
        recv_data = self.client.recv(8192)
        print(recv_data.decode('utf-8'))

    # def df(self, args):
    #
    #
    # def ls(self, args):
    #     pass

    # def mkdir(self, args):
    #     # print(args)
    #     recv_data = self.client.recv(8192).decode('utf-8')
    #     print(recv_data)

    # def cd(self, args):
    #     pass

    def put(self, args):
        print(args)
        upload_file = args.split()[1]
        if os.path.isfile(os.path.join(settings.upload_path, upload_file)):
            recv_data = self.client.recv(8192).decode('utf-8')
            print(recv_data)
            while True:
                recv_data = self.client.recv(8192).decode('utf-8')
                print(recv_data)
        else:
            print("文件不存在！")


    def get(self, args):
        pass


if __name__ =="__main__":
    Client()
    # print(Client().menu)