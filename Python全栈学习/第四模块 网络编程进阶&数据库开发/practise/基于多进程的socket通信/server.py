#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/25 16:55

from socket import *
from multiprocessing import Process

def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            print(data.decode())
            conn.send(b"hehehe")
        except Exception as e:
            print(e)
            break

def server():
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(('localhost', 9000))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        print(addr, " is connecting....")
        p = Process(target=talk, args=(conn,))
        p.start()




if __name__ == "__main__":
    server()

