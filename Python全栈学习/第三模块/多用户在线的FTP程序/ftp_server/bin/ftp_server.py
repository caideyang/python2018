#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 7:15
import socketserver
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)

from core import main
from conf import settings
# from modules.socket_server import  MyTCPHandler
if __name__ == "__main__":
    main.run() # 单线程版本

    # server = socketserver.ThreadingTCPServer((settings.ftp_server['IP'], settings.ftp_server['Port']), MyTCPHandler)
    # server.serve_forever()