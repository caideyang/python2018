#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/4 15:56

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

ATM_DIR = os.path.dirname(BASE_DIR)
ATM_ACCOUNTS_DIR = '%s/atm/db/accouts' % ATM_DIR

from core import main

if __name__ == "__main__":
    main.run()