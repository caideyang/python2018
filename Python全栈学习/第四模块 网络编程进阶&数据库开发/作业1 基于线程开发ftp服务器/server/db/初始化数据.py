#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 12:27

import os
import sys
import pickle

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BaseDir)
UploadsDir = os.path.join(BaseDir,'uploads')

from modules.users import  Users


name = 'caideyang'
password = 'e10adc3949ba59abbe56e057f20f883e' # 123456
quta = 1000   # 限额 1000M
cdy_obj = Users(name,password,quta)
with open(name, 'wb') as db_f:
    pickle.dump(cdy_obj, db_f)


name = 'deyangcai'
password = 'e10adc3949ba59abbe56e057f20f883e' # 123456
quta = 500   # 限额 500M
dyc_obj = Users(name,password,quta)
with open(name, 'wb') as db_f:
    pickle.dump(dyc_obj, db_f)




# if __name__ == "__main__":
#     with open(name, 'wb') as db_f:
#         pickle.dump(data, db_f)