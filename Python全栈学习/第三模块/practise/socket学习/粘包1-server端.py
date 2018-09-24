#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/20 7:23

import socket
server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen(5)
while True:
    conn, addr = server.accept()
    count = 1
    while True:
        data = conn.recv(15).decode('utf-8')
        if not data: break
        print('第%s次数据 %s' %(count, data))
        count += 1
    conn.close()