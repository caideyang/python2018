#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/9 20:02

import logging

fh = logging.FileHandler("mysql.log")
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(thread)d:%(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(ch)
logger.debug("hello ?")

if __name__ == "__main__":
    pass