#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 16:00

from socket import *
from threading import Thread

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
    server.listen(5)

    while True:
        conn, addr = server.accept()
        print(addr, " is connecting....")
        t = Thread(target=talk, args=(conn,))
        t.start()

if __name__ == "__main__":
    server("127.0.0.1", 9000)
