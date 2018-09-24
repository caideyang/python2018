#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from core.models_v2 import * #反序列化对象,必须保证类已经在内存中
from core import src
if __name__ == '__main__':
    src.run()