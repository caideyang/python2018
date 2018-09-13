#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 23:18

import os, sys

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BaseDir)

db = os.path.join(BaseDir, 'db', "school.dat")  # 创建数据保存文件路径

if __name__ == "__main__":
    pass