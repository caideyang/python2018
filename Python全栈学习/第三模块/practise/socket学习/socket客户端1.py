#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/18 21:56

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
while True:
    data = input("client: ").strip()
    client.send(data.encode('utf-8'))
    recvd_data = client.recv(1024).decode('utf-8')
    print(recvd_data)