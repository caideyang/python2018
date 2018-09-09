#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/6 6:55

import logging
logging.basicConfig(filename='log_test.log',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug("hello ")
logging.info("hello INFO")
logging.warn("Fcuk !")
logging.error("Server is error ")
logging.critical("Server is down")
