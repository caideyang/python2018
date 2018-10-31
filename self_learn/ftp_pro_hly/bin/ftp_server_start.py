#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Han Liyue"

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings

sys.path.append(settings.BASE_DIR)

if __name__ == '__main__':
    from core.ftp_server import MYTCPServer
    tcpserver1 = MYTCPServer(('127.0.0.1', 8088))

    tcpserver1.run()
    # MYTCPServer.run()