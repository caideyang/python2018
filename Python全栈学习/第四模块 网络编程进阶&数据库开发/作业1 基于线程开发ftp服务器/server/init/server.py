#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/22 9:52

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

if __name__ == "__main__":
    from core import management
    ftp_server = management.ManagementTool(sys.argv)
