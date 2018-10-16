#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/10/8 21:30
import pymysql

# 建立连接
conn = pymysql.connect(
    host = "47.92.222.189",
    port = 3306,
    user = 'cdy',
    password = 'cwq926823',
    db = 'db1',
    charset = 'utf8'
)
# 创建游标
cursor = conn.cursor()
# print(cursor)
username = input("username>>>")
password = input("password>>>")
sql = "select * from userinfo where name=%s and pwd=%s"
rows = cursor.execute(sql, (username, password))
if rows:
    print("登陆成功！")
else:
    print("登陆失败")
cursor.close()
conn.close()
if __name__ == "__main__":
    pass