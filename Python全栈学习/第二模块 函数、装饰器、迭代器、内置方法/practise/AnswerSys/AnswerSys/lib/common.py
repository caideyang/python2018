#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
import hashlib
import time
def create_id(*args):
    m=hashlib.md5()
    m.update(str(time.time()).encode('utf-8'))
    return m.hexdigest()











