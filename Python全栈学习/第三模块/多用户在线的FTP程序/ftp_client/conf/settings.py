#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 10:48

import os
import sys

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BaseDir)

ftp_server = {
    "IP"   :   "127.0.0.1",
    "Port" :   8888
}
upload_path = os.path.join(BaseDir, 'uploads')  # 需要上传到server端的文件存放的路径
download_path = os.path.join(BaseDir, 'downloads') # 从server端下载的文件存放的炉具

if __name__ == "__main__":
    pass