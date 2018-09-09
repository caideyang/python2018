#!_*_coding:utf-8_*_
#__author__:"Alex Li"

"""
银行账号管理
    用户认证
    账户间转账
    每月账单记录、查看
    还款操作
    取款操作


"""

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from core import main

if __name__ == '__main__':

    main.run()
