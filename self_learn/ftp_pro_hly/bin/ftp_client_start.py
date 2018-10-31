#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Han Liyue"

import sys
from 网络编程进阶.ftp_pro_优化版.conf import settings

sys.path.append(settings.BASE_DIR)


if __name__ == '__main__':

    from core.ftp_client import MYTCPClient
    client = MYTCPClient(('192.168.1.7', 8080))
    client.run()