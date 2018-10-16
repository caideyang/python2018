#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/26 16:00

from socket import *
client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost", 9000))
while True:
    data = input(">>>").strip()
    client.send(data.encode('utf-8'))
    data = client.recv(1024).decode('utf-8')
    print(data)

if __name__ == "__main__":
    pass