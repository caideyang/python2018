#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/10/10 16:26

from gevent import monkey; monkey.patch_all()
from socket import  *
import  gevent


def start_server(host, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((host, port))
    server.listen(500)
    while True:
        conn, addr = server.accept()
        gevent.spawn(task, conn, addr)


def task(conn , addr):
    print(addr, "连接....")
    while True:
        try:
            recv_data = conn.recv(1024)
            if not recv_data:
                conn.close()
                print(addr, "断开连接")
                break
            print(recv_data.decode())
            conn.send(recv_data.upper())
        except Exception:
            print(addr, "断开连接")
            conn.close()
            break


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 9000
    start_server(host, port)