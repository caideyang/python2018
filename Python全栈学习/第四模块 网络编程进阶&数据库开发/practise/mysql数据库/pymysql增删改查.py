#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/10/9 10:25

import pymysql

# 创建连接
conn = pymysql.connect(
    host = "47.92.222.189",
    port = 3306,
    user = "cdy",
    password = "cwq926823",
    db = "db1",
    charset = "utf8"
)
# 创建游标
cursor = conn.cursor()

#  增
sql = "insert into userinfo (name, pwd) values (%s, %s)"
res = cursor.execute(sql,('cdy6','6666'))  # 新增一行
print(cursor.lastrowid) # 获取插入的最后一条数据的自增ID,
# res = cursor.executemany(sql,[('cdy9', '9988'),('cdy10', '8108')])  # 新增多行


#  删
# sql = "delete from t1 where id = %s"
# condition = input("请输入要删除的id: ").strip()
# res = cursor.execute(sql,(condition, ))
# print(sql)

# 改
# sql = "update userinfo set pwd = %s where id = %s"
# condition = input("请输入要修改的id: ").strip()
# pwd = input("请输入新密码:").strip()
# res = cursor.execute(sql,(pwd, condition))

# 执行增删改以后，需要对数据进行commit操作，否则执行不成功。
conn.commit()
if res:
    print("操作成功，受影响%s行" % res)
else:
    print("操作失败")

# 查


# condition = input("要查询的条件：").strip()
# sql = "select *  from  userinfo where id > %s "
# res = cursor.execute(sql, (condition, ))
# if res:
#
#     # cursor.scroll(3,mode='relative') # 相对当前位置移动
#     print(cursor.fetchone()) # 取一行
#     # cursor.scroll(3,mode='absolute') # 相对绝对位置移动
#     cursor.scroll(3,mode='relative') # 相对当前位置移动
#     print(cursor.fetchone()) # 取一行

    # print(cursor.fetchmany(2)) # 取多行
    # print(cursor.fetchall()) # 全部取出
# else:
#     print("No records!")
cursor.close()
conn.close()
if __name__ == "__main__":
    pass