#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Han Liyue"
import socket
import struct
import json
import subprocess
import os
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


from conf import settings
from core import myHead
db = '%s\db\\'%settings.BASE_DIR
print("\033[1;36;49m服务端：start... ...\033[m")

class MYTCPServer:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding='utf-8'
    request_queue_size = 5

    def __init__(self, server_address, bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        self.server_address=server_address
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if bind_and_activate:      # 通讯链接循环
            try:
                self.server_bind()
                self.server_activate()
            except:
                self.server_close()
                raise

    def server_bind(self):
        """Called by constructor to bind the socket.
        """
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_activate(self):
        """Called by constructor to activate the server.
        """
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        """Called to clean-up the server.
        """
        self.socket.close()

    def get_request(self):
        """Get the request and client address from the socket.
        """
        return self.socket.accept()

    def close_request(self, request):
        """Called to clean up an individual request."""
        request.close()

    def communicate(self,conn):
        print(conn)
        while True:  # 通讯循环
            print(1)
            try:
                head_struct = conn.recv(4)
                print(2,head_struct)
                if not head_struct: break

                head_len = struct.unpack('i', head_struct)[0]
                print(3,head_len)
                head_json = conn.recv(head_len).decode(self.coding)
                print(4,head_json)
                head_dic = json.loads(head_json)
                print(5,head_dic)

                # print(head_dic)
                # head_dic={'cmd':'put','filename':'a.txt','filesize':123123}
                cmd = head_dic['action_type']  # 通过抓取用户输入的操作类型名称进行反射
                print(6,cmd)
                # print(cmd)
                if hasattr(self, cmd):
                    print(7,cmd)
                    func = getattr(self, cmd)
                    print(8,head_dic)
                    func(head_dic)  # 反射：执行相应的指令函数
                    print(1111111)
            except Exception:
                break

    def run(self):
        while True:
            conn,client_addr=self.get_request()
            print(conn,'from client ',client_addr)
            # poll = ProcessPoolExecutor(3)
            # poll.submit(self.communicate,)
            # poll.shutdown()
            # for i in range(5):
            t = Thread(target=self.communicate,args=(conn,))
            t.start()



    # 查询目录
    def dir(self, args,conn):
        print(1,'get方法')
        cmd = args['action_type']   # 取出报头字典里'action_type'的值
        print(2,cmd)   # dir

        # 获得db的路径
        res = subprocess.Popen('%s %s' % (cmd, db),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        print(3)
        err = res.stderr.read()
        print(4)
        # print(err)
        if err:
            back_msg = err
        else:
            back_msg = res.stdout.read()

        headers = {'data_size': len(back_msg)}
        print(5)
        head_json = json.dumps(headers)
        print(6)
        head_json_bytes = bytes(head_json, encoding='utf-8')
        print(7)

        conn.send(struct.pack('i', len(head_json_bytes)))  # 先发报头的长度
        print(8)
        conn.send(head_json_bytes)  # 再发报头
        print(9)
        conn.sendall(back_msg)  # 再发真实的内容
        print(10)

    # 文件上传
    def put(self,args,conn):
        filename1 = args['filename']
        # print(filename1)
        filename = os.path.split(filename1)[-1]  # 这是文件名，即报头里取值最后一个
        print(filename)

        file_path=os.path.join(     # 文件上传地址路径
            settings.upload_dir,
            filename
        )
        # print(file_path)  # C:\Users\Administrator\Desktop\ftp_pro\db\upload\123.py

        filesize=args['file_size']  # 取出文件大小
        # print(filesize)
        recv_size=0
        # print('----->',file_path)
        # print('开始接收上传的文件！')
        with open(file_path, 'wb') as f:
            # print('开始读写！')
            while recv_size < filesize:
                recv_data=conn.recv(self.max_packet_size)
                f.write(recv_data)   # 将接收的内容循环写进新创建文件里
                srecv_size+=len(recv_data)
                print('已上传大小:%s 文件总大小:%s' %(recv_size,filesize))

    # 文件下载
    def get(self,args,conn):
        # print("为什么不执行呢。。。。")
        cmd = args['action_type']   # 取出命令类型“get”
        filename = args['filename']
        # print(cmd,filename)

        filename1 = os.path.join(settings.share_dir,filename)   # 下载文件路径
        # print(filename,filename1)
        filesize = os.path.getsize(filename1)
        # print(filesize)

        head_dic = myHead.head(cmd,filename,filesize)
        print(head_dic)

        head_json=json.dumps(head_dic)
        head_json_bytes=bytes(head_json,encoding=self.coding)
        head_struct=struct.pack('i',len(head_json_bytes))

        # print("发发发。。。")
        conn.send(head_struct)
        conn.send(head_json_bytes)

        # 开始发送文件
        send_size = 0
        with open(filename1, 'rb') as f:
            for line in f:
                conn.send(line)
                send_size += len(line)
                print(send_size)
            else:
                print('upload successful')

# s = MYTCPServer(('192.168.1.7', 8080))
# s.run()
