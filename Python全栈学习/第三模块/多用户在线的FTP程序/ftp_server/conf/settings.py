#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/13 17:57

import os
import sys

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BaseDir)

db = os.path.join(BaseDir, 'db')  # 创建数据保存文件路径

Ftp_Base_Dir = 'uploads'
UploadsDir = os.path.join(BaseDir, Ftp_Base_Dir)


ftp_server = {
    "IP"   :   "127.0.0.1",
    "Port" :   8888
}

if __name__ == "__main__":
    print(db)
    print(UploadsDir)