#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/5 9:51

import datetime
import json

# 获取实时时间，并格式化
def get_current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 设置字体高亮
def set_color(item):
    return "\033[31m"+str(item)+"\033[1m"


# 保存json数据
def save_database(database,file):
    with open(file,"w") as f:
        json.dump(database,f)


# 获取json数据
def load_database(file):
    with open(file,"r") as f:
        database = json.load(f)
    return database