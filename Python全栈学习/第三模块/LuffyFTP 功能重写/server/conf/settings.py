#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/22 9:49

import os
import sys

HOST = '0.0.0.0'
PORT = 9000

MAX_CLIENT_COUNT = 5
MAX_RECV_BYTE = 8192
DEFAULT_BYTE_CODE = 'utf-8'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_BASE_DIR = 'uploads'
# USER_ACCOUNT_FILE = os.path.join(BASE_DIR, 'conf', 'account.ini')

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
# sys.path.append(BaseDir)

db = os.path.join(BaseDir, 'db')  # 创建数据保存文件路径