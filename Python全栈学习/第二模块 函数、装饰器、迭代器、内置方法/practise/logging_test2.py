#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/9 19:40

import logging



# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(filename)s - %(levelname)s - %(thread)d:%(message)s' )
# logging.info("hello ?")
# logging.debug("hello debug ?")
# logging.critical("Hello ")


logging.basicConfig(filename='test2.log',level=logging.INFO,
                    format='%(asctime)s - %(filename)s - %(levelname)s - %(thread)d:%(message)s')
logging.info("wenjain info")
logging.warning("wenjain info")
logging.error("wenjain info")


if __name__ == "__main__":
    pass