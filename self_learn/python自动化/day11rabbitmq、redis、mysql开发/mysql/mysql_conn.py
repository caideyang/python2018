#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/31 14:38

import pymysql  #pip install pymysql
#创建连接
conn = pymysql.connect(host="192.168.56.11",port=3306,user="cdy",passwd="passwd",db="test")
cursor = conn.cursor()#创建游标
effect_row = cursor.execute("select * from t1")#执行sql，返回受到影响的行
print(cursor.fetchone()) #一条一条取数据
print(cursor.fetchmany(3)) #取前3条数据
print(cursor.fetchall()) #取剩余所有数据

# db = [(3,"xiaocai"),
#         (4,"xiaozhou"),
#         (9,"xiaoyu")]
# cursor.executemany("insert into t1 values  (%s,%s)",db) #批量插入数据

conn.commit() #提交，否则无法保存新建或者修改的数据
cursor.close()#关闭游标
conn.close()#关闭连接