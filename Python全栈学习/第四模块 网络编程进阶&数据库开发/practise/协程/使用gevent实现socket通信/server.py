#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 16:00
from gevent import monkey; monkey.patch_all()
from socket import *
import gevent
def talk(conn):
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data: break
            print(data)
            conn.send(data.upper().encode('utf-8'))
        except Exception as e:
            print(e)
            break

def server(host, port):
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(50)
    while True:
        conn, addr = server.accept()
        print(addr, " is connecting....")
        gevent.spawn(talk, conn)

if __name__ == "__main__":
    server("127.0.0.1", 9000)
