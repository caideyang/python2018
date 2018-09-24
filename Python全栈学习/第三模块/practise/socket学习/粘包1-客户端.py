#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/20 7:23

import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))
while True:
    time.sleep(0.0000000011)
    client.send("hello".encode('utf-8'))




client.close()