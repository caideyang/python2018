#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 7:20

import socket
import pickle
from controller.ftp_manage import FtpManage
from conf import settings


def run():

    HOST, PORT = settings.ftp_server['IP'], settings.ftp_server['Port']
    # HOST, PORT = '127.0.0.1', 8888
    server = socket.socket()
    print("正在启动FTP服务，端口【%s】。。。。" % PORT)
    try:
        server.bind((HOST, PORT))
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.listen(10)
        print("启动FTP服务成功，端口【%s】。" % PORT)
        while True:
            # print("1111111111111111111111")
            conn, addr = server.accept()
            cli = FtpManage(conn)
            print(conn, addr)
            while True:
                # print("2222222222222222222")
                try:
                    recv_data = pickle.loads(conn.recv(8192))
                    if not recv_data: break
                    print(recv_data)
                    action = recv_data['action']
                    request = recv_data['request']
                    # print(action,request)
                    if hasattr(cli, action):
                        msg = getattr(cli, action)(request)
                        conn.send(msg)
                    else:
                        conn.send(pickle.dumps("Error!"))
                except EOFError :
                    getattr(cli, "logout")("")
                    break
            conn.close()
    except OSError as e:
        print("OSError: %s ,端口【%s】被占用,启动失败！" % (e.errno, PORT))
if __name__ == "__main__":
    pass