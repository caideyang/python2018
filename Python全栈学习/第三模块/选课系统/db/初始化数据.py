#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 23:38
import pickle
import os
import sys
BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BaseDir)

from modules.school import  School

data = {}
name = 'OldBoy北京校区'
addr = '北京'
bj_obj = School(name,addr)
data[name] = bj_obj

name = 'Oldboy上海校区'
addr = '上海'
sh_obj = School(name,addr)
data[name] = sh_obj




if __name__ == "__main__":
    with open('school.dat', 'wb') as db_f:
        pickle.dump(data, db_f)