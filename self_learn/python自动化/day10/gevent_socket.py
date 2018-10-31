#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/25 14:39

import gevent,socket
from gevent import monkey
monkey.patch_all()

def server(port):
    s = socket.socket()
    s.bind(("localhost",port))
    s.listen(50)
    print("Port %s is listening...." % port)
    while True:
        conn,addr = s.accept()
        print("一个连接%s已经建立" % addr[1])
        gevent.spawn(handle_request,conn,addr)

def handle_request(conn,addr):
    try:
        while True:
            data = conn.recv(1024).decode()
            print("Recv from %s: %s "%(addr[1],data))
            conn.send(data.encode())
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    server(9000)