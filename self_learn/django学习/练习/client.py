#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/10/30 14:52

from socket import *

client = socket(AF_INET, SOCK_STREAM)
host = "g.cn"
port = 80

client.connect((host, port))
http_request = ""

if __name__ == "__main__":
    pass