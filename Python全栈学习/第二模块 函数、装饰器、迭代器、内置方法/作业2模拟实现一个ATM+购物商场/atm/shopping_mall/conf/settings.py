#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/4 16:08

import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ATM_DIR = os.path.dirname(BASE_DIR)

DATABASE = {
    'shopping' : '%s/db' % BASE_DIR,
    'atm' : '%s/atm/db/accounts' % ATM_DIR
}

products = {
        "1":{"name": "电脑", "price": 1999},
        "2":{"name": "鼠标", "price": 100},
        "3":{"name": "游艇", "price": 20000},
        "4":{"name": "美女", "price": 998},
        "5":{"name": "粪叉", "price": 6688},
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': '%s/log/transactions.log' % BASE_DIR,
    'access': '%s/log/access.log' % BASE_DIR,
    'pay': '%s/atm/log/transactions.log' % ATM_DIR,
    'pay_auth': '%s/atm/log/access.log' % ATM_DIR
}

TRANSACTION_TYPE = {
    'consume':{'action':'minus', 'interest':0},
}