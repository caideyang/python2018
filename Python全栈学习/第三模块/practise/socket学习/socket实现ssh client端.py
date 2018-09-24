#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/19 22:18

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8888))

while True:
    cmd = input(">").strip()
    if not cmd: continue
    client.send(cmd.encode('utf-8'))
    flag = True
    while flag:
        res = client.recv(1024)
        if len(res) < 1024:
            flag = False
        print(res.decode('gbk'))
