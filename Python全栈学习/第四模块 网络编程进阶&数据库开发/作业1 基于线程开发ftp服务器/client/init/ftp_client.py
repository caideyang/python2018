#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/22 20:24
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)

from core import socket_client

if __name__ == "__main__":
    socket_client.FTPClient()

