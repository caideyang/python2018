#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 13:49

import time
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
        if not os.path.isfile(data):
            return None
        with open(data,'rb') as f:
            for line in f:
                m.update(line)
    else:
        exit("Type error !")
    return m.hexdigest()

#定义一个进度条
import sys
def process_bar(num, total):
    rate = float(num) / total
    ratenum = int(rate * 100)
    r = '\r[{}{}]已传输完成{}，{}%'.format('*' * ratenum + ">",  ' ' * (100 - ratenum), num, ratenum)
    sys.stdout.write(r)
    sys.stdout.flush()

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
                   logout. 断开连接
               """
        self.menu_dict = {
            "pwd": self.pwd,
            "df": self.df,
            "ls": self.pwd,
            "mkdir": self.pwd,
            "cd": self.pwd,
            "put": self.put,
            "get": self.get,
            "logout": self.logout
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
                commands = input("请输入您要执行的命令：").strip()
                if not commands: continue
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
            recvd_data = self.client.recv(8192)
            recvd_data = pickle.loads(recvd_data)
            # print(type(recvd_data))
            self.is_certified = recvd_data['is_certified']
            if self.is_certified:
                print("FTP服务器认证通过，登陆成功！")
                self.name = request['name']
                while True:
                    print(self.menu)
                    messages = input("请输入您要执行的命令：").strip()
                    if not messages: continue
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
        exit(0)


    def pwd(self, args):
        # print(args)
        recvd_data = self.client.recv(8192)
        print(recvd_data.decode('utf-8'))

    def df(self, args):
        recvd_data = self.client.recv(8192)
        # print(recvd_data)
        msg = pickle.loads(recvd_data)
        print("空间限额：【%s】MB  已使用空间：【%s】MB 剩余空间: 【%s】 MB" %(msg['quota'], msg['used_space'], msg['aviable_space']))



    # def ls(self, args):
    #     pass

    # def mkdir(self, args):
    #     # print(args)
    #     recvd_data = self.client.recv(8192).decode('utf-8')
    #     print(recvd_data)

    # def cd(self, args):
    #     pass

    def put(self, args):
        """
        1.判断本地文件是否存在，存在则把本地文件相关信息发给服务器端，等待服务器响应
        send {"filename":"1.jpg", "filesize":123456, "file_md5":"abcdefg",'status':True }
        3. 根据服务端响应做出相应的操作
        3.1 如果服务器不存在该文件，则直接上传，如果存在且Md5相同，则不上传，如果存在，且md5不相同，则上传
        3.2 用户选择是否覆盖还是重传
        3.3 提交客户端端响应数据
        send {"filename":"1.jpg","filesize":123456, "file_md5":"abcdefg","seek_size":1112,  }
        5. 开始发送数据，当文件传输完毕时关闭文件，等待服务端返回上传的结果
        7.获取md5结果，结束上传
        """
        filename = args[1]
        abs_file_path = os.path.join(settings.upload_path, filename)
        file_md5 = get_md5(abs_file_path, type='file')
        if file_md5: # 文件存在
            filesize = os.path.getsize(abs_file_path)
            send_msg = {"filename":filename, "filesize":filesize, "file_md5": file_md5,"status": True}
            self.client.send(pickle.dumps(send_msg))

            recvd_data = pickle.loads(self.client.recv(8192)) # 3. 根据服务端响应做出相应的操作
            if recvd_data['server_file_md5'] == file_md5:
                print("对应文件已经存在，且内容一致！！！！")
                seek_size = -1
                # print(22222222222222)
                # msg = self.client.recv(8192)
                # print(msg)
            elif recvd_data['space_aviable'] <= 0 :
                print("服务器可用空间不足！")
            else:
                if recvd_data['server_file_md5']: # 服务器有该文件，但内容不全
                    print(recvd_data)
                    seek_place = recvd_data['filesize']
                    choice = input("是否覆盖？1-覆盖，0-续传").strip()
                    if choice == '1':
                        seek_size = 0
                    else:
                        seek_size = recvd_data['filesize']
                else: #服务器无该文件
                    seek_size = 0
                send_msg['seek_size'] = seek_size
                self.client.send(pickle.dumps(send_msg)) # 3.3 提交客户端端响应数据
                to_send_size = filesize - seek_size  # 需要发送的字节数
                with open(abs_file_path, 'rb') as f:
                    f.seek(seek_size)
                    while to_send_size > 0 :
                        self.client.send(f.read(8192))
                        time.sleep(0.000001)
                        to_send_size -= 8192
                        seek_size = filesize - to_send_size
                        # print(seek_size)
                        process_bar(seek_size, filesize)
                print("传输完成！")
                recvd_data = pickle.loads(self.client.recv(8192))  # 7. 获取服务端返回的传输状态
                if recvd_data['status'] == 1:
                    print("传输成功，md5校验通过！")
                else:
                    print("传输成功，md5校验失败！")

        else:
            print("文件不存在！")
            send_msg = {"filename": filename, "status": False}
            self.client.send(pickle.dumps(send_msg))  # 3.3 提交客户端端响应数据

        # msg = self.client.recv(8192)
        # print(msg)

    def get(self, args):
        filename = args[-1]
        abs_file_path = os.path.join(settings.download_path, filename)
        file_md5 = get_md5(abs_file_path, type='file')
        res = pickle.loads(self.client.recv(8192))
        if res['status'] == -1:
            print(res['msg'])
        elif res['status'] == 1:
            # 可以开始正常传输,判断本地是否有该文件
            server_file_size = res['file_size']
            if os.path.isfile(abs_file_path):
                file_size = os.path.getsize(abs_file_path)
                #判断是否覆盖，如果不覆盖,则续传，seek_place = file_size
                choice = input("是否覆盖：0-覆盖，1-续传").strip()
                if choice == '0':
                    seek_place = 0
                    f = open(abs_file_path, 'wb')
                else:
                    seek_place = file_size
                    f = open(abs_file_path, 'ab')
            else:
                seek_place = 0
                f = open(abs_file_path, 'wb')

            msg = {"status": 0, "seek_place": seek_place, "msg": "准备完成，可以传输！"}
            self.client.send(pickle.dumps(msg))
            while seek_place < server_file_size:
                # if file_md5 == res['md5']:
                #     break
                data = self.client.recv(8192)
                # print(data)
                f.write(data)
                seek_place += 8192
                process_bar(seek_place, server_file_size)
            # print("传输完成")

                # if seek_place >=  server_file_size:
                #     print("传输完成")
                #     flag = False
            f.close()
            new_file_md5 = get_md5(abs_file_path, "file")
            if new_file_md5 == res['md5']:
                print("传输完成,md5校验通过！")
            else:
                print("传输完成，md5校验失败！")

    def logout(self, args):
        print("退出")
        self.client.close()
        exit(0)

if __name__ =="__main__":
    Client()
    # print(Client().menu)