#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 21:59

# settings

import os, sys

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BaseDir)

school_db = os.path.join(BaseDir, 'db', "school")  # 创建数据保存文件路径