#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 21:58


# 启动
import os, sys

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BaseDir)
from core.main import home

if __name__ == "__main__":
    home.show_home()