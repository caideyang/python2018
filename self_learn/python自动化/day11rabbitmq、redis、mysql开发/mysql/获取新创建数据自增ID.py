#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/31 14:51


import pymysql

conn = pymysql.connect(host="192.168.56.11",port=3306,user="cdy",passwd="passwd",db="test")
cursor = conn.cursor()
cursor.executemany("insert into class (caption)values(%s)", [("一年级一班"), ("一年级二班"),("二年级一班"),("二年级二班"),("三年级1班"),])
conn.commit()
cursor.close()
conn.close()

# 获取最新自增ID
new_id = cursor.lastrowid
print(new_id)  #这个不准

import random
print(random.choice(["F","M"]))