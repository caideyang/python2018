#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Han Liyue"


import os
import sys

# 环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

# 用户的信息文件
account_file = '%s\\conf\\account.cfg' % BASE_DIR

# 用户个人目录
public_list = '%s\\userspace\\' % BASE_DIR
# print(public_list)

# 用户信息存储路径
user_info_dir= '%s\\userspace\\user_info' % BASE_DIR
# print(user_info_dir)

# 文件上传之接收地址路径
upload_dir = '%s\\db\\upload'%BASE_DIR
# print(upload_dir)

# 文件下载之接收地址路径
download_dir= '%s\\db\\download'%BASE_DIR
# print(download_dir)

# 文件下载路径
share_dir = '%s\\db\\share'%BASE_DIR
# print(share_dir)

# 用户个人文件下载路径
# user_dw_dir = '%s\\userspace\\%s'%(BASE_DIR,username)



