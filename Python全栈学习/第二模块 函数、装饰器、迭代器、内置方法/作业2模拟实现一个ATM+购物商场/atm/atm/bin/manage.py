#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/28 11:36

"""
管理员账号登陆
管理员功能：
    添加银行账户
    查看银行账户
    修改账户信息
    冻结账户

"""

import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import admin

if __name__ == '__main__':
    admin.run()