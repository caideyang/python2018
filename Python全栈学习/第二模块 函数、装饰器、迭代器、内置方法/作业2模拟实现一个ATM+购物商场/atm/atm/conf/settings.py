#!_*_coding:utf-8_*_
#__author__:"Alex Li"
import os
import sys
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# print(BASE_DIR)

DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR
}

ADMIN = {
    'name': "admin",
    'password': 'e10adc3949ba59abbe56e057f20f883e' # 123456
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
    'manage': 'manage.log',
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},

}
# 中英文对照字典
# DIRECTORY = {
#     "account": "账号",
#     "amount": "金额",
#     "action" : "交易类型",
#     "repay": "还款",
#     "withdraw": "取现",
#     "interest": "利息/手续费",
#     "transfer": "转账",
#     "consume": "消费",
#
# }