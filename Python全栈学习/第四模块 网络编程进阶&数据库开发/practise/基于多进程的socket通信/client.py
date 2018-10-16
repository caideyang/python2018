#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/25 16:55

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 9000))
while True:
    data = input(">>> ").strip()
    client.send(data.encode())
    res = client.recv(1024)
    print(res.decode())