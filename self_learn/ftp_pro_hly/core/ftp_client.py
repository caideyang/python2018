#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Han Liyue"

import hashlib
import socket
import struct
import json
import os
import subprocess
from threading import Thread
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

from 网络编程进阶.ftp_pro_优化版.core import myHead
from 网络编程进阶.ftp_pro_优化版.conf import settings
print("\033[1;33;46m客户端：start... ...\033[m")
info = [
        {"order": "查看目录：dir"},
        {"order": "上传文件：put 123.py/柏拉图.txt/扁豆.jpg/菠菜.jpg/萝卜.jpg"},
        {"order": "下载文件：get 白菜.jpg/龙猫1.jpg/龙猫2.jpg/龙猫3.jpg"},
        {"order": "退出：Q"},
        ]
# 用户查看执行命令函数
def see():
    print("\033[1;35;44m ----- 【温馨提示】----- \033[m")
    for index, i in enumerate(info):
        print(index+1, i.get("order"))

class MYTCPClient:
    address_family = socket.AF_INET       # 地址家族
    socket_type = socket.SOCK_STREAM      # 通讯类型 TCP
    allow_reuse_address = False           # IP地址重用状态
    max_packet_size = 8192
    coding='utf-8'                        # 编码类型：utf-8
    request_queue_size = 5                # 代表最大挂起的连接数 5

    def __init__(self, server_address, connect=True):
        self.server_address=server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if connect:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise

    def client_connect(self):
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()

    def run(self):
        m = hashlib.md5()  # 密码通过md5加密
        user = input(">>>User_name:")
        psd = input(">>>User_Psd:")
        psd_bytes = bytes(psd, encoding="utf-8")  # 转换用户输入密码为bytes格式，以便运算MD5值
        m.update(psd_bytes)
        m1 = m.hexdigest()  # 转化用户输入密码为MD5值，以便与数据库信息比对

        with open(settings.user_info_dir, "r", encoding="utf-8") as f:
            for line in f:
                name, password, md5,size = line.strip().split("|")
                if user == name and m1 == md5:
                    print("Welcome to FTP Homely")
                    see()
                    while True:
                        inp=input("请您按照以上提示输入执行命令>>: ").strip()
                        if not inp:continue
                        if inp == "Q": exit()
                        l=inp.split()
                        cmd=l[0]
                        if hasattr(self,cmd):
                            func=getattr(self,cmd)
                            func(l)
                        # elif inp == "Q":
                        #     print("程序已退出")
                        #     break
            else:
                print("\033[1;35;44m wrong name or psd ！ \033[m")

    # 查看目录
    def dir(self, args):
        # print("ccccc")
        cmd = args[0]  # dir
        print(cmd)

        head_dic = myHead.head(cmd)    # 调用myHead.py之head函数方法，简化报头字典的代码量，并将cmd作为用户输入的指令传参
        print(head_dic)

        head_json = json.dumps(head_dic)   # 把报头进行序列化，转换为字符串格式以便文件传输
        print(head_json)
        head_json_bytes = bytes(head_json, encoding=self.coding)    # 将报头再转换为bytes格式进行传输
        print(head_json_bytes)

        head_struct = struct.pack('i', len(head_json_bytes))    # 固定报头长度，以便传输
        print(head_struct)
        self.socket.send(head_struct)    # 发送报头固定长度
        print("ccccc")
        self.socket.send(head_json_bytes)    # 以bytes格式传送报头真是内容
        print('指令发送完成')

        head = self.socket.recv(4)  # 先收4个bytes，这里4个bytes里包含了报头的长度
        print(1)
        head_json_len = struct.unpack('i', head)[0]  # 解出报头的长度
        print(2)
        head_json = json.loads(self.socket.recv(head_json_len).decode(self.coding))  # 拿到报头内容
        print(3)
        data_len = head_json['data_size']  # 取出报头内包含的信息，确定其大小
        print(4)

        # 开始收数据
        recv_size = 0
        recv_data = b''
        while recv_size < data_len:
            recv_data += self.socket.recv(self.max_packet_size)
            recv_size += len(recv_data)

        print(recv_data.decode('gbk'))

    # 文件上传
    def put(self,args):
        cmd=args[0]
        filename=args[1]
        # print(cmd,filename)
        # 需要添加路径
        file_path = '%s\\%s'%(settings.public_list, 'admin')
        # print(file_path)

        # 把目录和文件名结合起来
        newFilename = os.path.join(file_path, filename)
        # print(newFilename)

        if not os.path.isfile(newFilename):
            print('file:%s is not exists' % newFilename)
            return
        else:
            # 获取文件大小
            filesize=os.path.getsize(newFilename)

        head_dic = myHead.head(cmd, newFilename, filesize)

        head_json=json.dumps(head_dic)
        head_json_bytes=bytes(head_json,encoding=self.coding)

        # 固定报头长度
        head_struct=struct.pack('i',len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)

        # 开始发送文件
        send_size=0
        with open(newFilename,'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size+=len(line)
                print(send_size)
            else:
                print('upload successful')

    # 文件下载
    def get(self,args):
        cmd = args[0]
        # print(cmd)
        filename = args[1]

        # 发送需求指令
        head_dic = myHead.head(cmd,filename)
        print(head_dic)
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json, encoding=self.coding)

        head_struct = struct.pack("i",len(head_json_bytes))
        # print("发送执行命令")
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)

        # 需要添加文件下载路径
        file_path = '%s\\%s' % (settings.download_dir, filename)
        # print(file_path)

        # print("开始接收消息")
        obj = self.socket.recv(4)
        header_size = struct.unpack("i", obj)[0]  # 解析出报头的长度
        header_bytes = self.socket.recv(header_size)  # 解读出报头内容

        header_json = header_bytes.decode("utf-8")  # 将bytes 格式转换为字符串信息，以便loads
        header_dic = json.loads(header_json)
        # print(header_dic)
        total_size = header_dic["file_size"]
        # print(total_size)
        # filename = header_dic["filename"]

        # 开始收文件
        recv_size = 0
        # print("打开新建文件")
        with open(file_path, "wb") as f:
            # print("打开文件开始写...")
            while recv_size < total_size:
                line = self.socket.recv(self.max_packet_size)
                f.write(line)
                # print("写进去啦。。。")
                recv_size += len(line)
                print("总大小:%s,已下载：%s,下载进度：%s" % (total_size, recv_size, (recv_size / total_size) ))


# c = MYTCPClient(('192.168.1.7', 8080))
# c.run()