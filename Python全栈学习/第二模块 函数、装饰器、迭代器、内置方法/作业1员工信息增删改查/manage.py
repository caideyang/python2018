#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/28 11:36

import datetime
import shutil
import re

useage = """
Usage:
    1.查询语法:
    find name,age from staff_table where age > 22
    find * from staff_table where dept = "IT"
    find * from staff_table where enroll_date like "2013"
    find * from staff_table where name like "Alex"
    find staff_id,name,age,enroll_date from staff_table where enroll_date like "2013"
    ...
    2.创建新员工：
    add staff_table Alex Li,25,134435344,IT,2015‐10‐29
    
    3.删除指定员工信息纪录，输入员工id，即可删除
    语法: del from staff_table where staff_id > 3
          del from staff_table where name like "Alex"
          ...
    4.修改员工信息，语法如下:
    update staff_table set dept="Market" where dept = "IT" 把所有dept=IT的纪录的dept改成Market
    update staff_table set age=25 where name = "Alex Li" 把name=Alex Li的纪录的年龄改成25
    update staff_table set name=Deyang Cai where phone = "134435344"
    ...
"""

# 获取员工信息表内容
def get_info(file="employee_info"):
    database = []
    with open(file, 'r',encoding="utf-8") as f:
        for employ_info in f.readlines():
            employ_info = employ_info.strip()
            database.append(employ_info.split(','))
    return  database

# 存取员工信息表内容
def save_info(database, file='employee_info'):
    now = datetime.datetime.now().strftime('%Y%m%d%H%M')
    shutil.copy(file, file+now) # 备份
    with open(file, 'w+') as f:
        for data in database:
            f.write(",".join(data)+"\n")

# 根据where条件过滤
def condition(database, sql_list):
    title = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']
    # print(sql_list[7].strip('"'))
    if len(sql_list) > 8:  # 当根据名字查询，可能有空格，则把列表最后两位合成一个字段处理
        sql_list[7] = " ".join(sql_list[7:])
        # print(sql_list)
    elif len(sql_list) < 8:
        exit("查询语句语法有误，请重试！")
    try:
        if sql_list[6] == '>':
            result = [data for data in database if int(data[title.index(sql_list[5])]) > int(sql_list[7])  ]
        elif sql_list[6] == '=':
            result = [data for data in database if data[title.index(sql_list[5])] == sql_list[7].strip("'").strip('"') ]
        elif sql_list[6] == '<':
            result = [data for data in database if int(data[title.index(sql_list[5])]) <  int(sql_list[7]) ]
        elif sql_list[6] == 'like':
            result = [data for data in database if  re.search(sql_list[7].strip('"').strip("'"),data[title.index(sql_list[5])]) ]
        return result
    except:
        exit("查询条件有问题,请核对后重试！")


# 增
def add(database, sql):
    sql_list = sql.split(",")
    staff_id = str(int(database[-1][0]) + 1) # 获取最新的staff_id
    name = sql_list[0].split(" ",2)[-1]
    new_staff = [staff_id,name]  # 新增用户信息表
    new_staff.extend(sql_list[1:])
    phone = sql_list[2]
    phone_list = [data[3] for data in database ]
    if phone not in phone_list: # 判断手机号是否唯一
        database.append(new_staff)
        # print(database)
        save_info(database)
        print("新增1条用户信息成功")
    else:
        print("电话号码冲突，保存信息失败！")


# 删
def delete(database, sql):
    # print(sql)
    where_condition = sql.split("where")[1]
    find_sql = "find * from staff_table where " + where_condition
    # print(find_sql)
    find_data = condition(database,find_sql.split())

    if len(find_data) == 0:
        print("未找到对应的记录，删除【0】条记录")
    else:
        find_staff_list = [data[0] for data in find_data]
        staff_list = [data[0] for data in database]
        for staff_id in find_staff_list:
            index = staff_list.index(staff_id)
            del staff_list[index]
            del database[index]
        save_info(database)
        print("删除【%s】条记录成功！" % len(find_data))


# 改
def update(database, sql):
    # update staff_table set age=25 where name = "Alex Li"
    title = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']
    where_condition = sql.split("where")[1]  # 查询条件 name = "Alex Li"
    update_data = sql.split("where")[0].split("set")[1]   #  age= 25
    field = update_data.split("=")[0].strip()  # 需要修改的field，此处为age
    # print(field)
    value = update_data.split("=")[1].strip().strip("'").strip('"')  # 需要修改成的值，此处为 25
    if field not in title:
        exit("需要修改的列不存在，修改失败！")
    field_index = title.index(field)
    find_sql = "find * from staff_table where "+ where_condition
    find_data = condition(database, find_sql.split())
    if len(find_data) == 0:
        print("未找到对应的记录，修改【0】条记录")
    else:
        find_staff_list = [data[0] for data in find_data]
        staff_list = [data[0] for data in database]
        for staff_id in find_staff_list:
            index = staff_list.index(staff_id)
            database[index][field_index] = value #修改语句
        save_info(database)
        print("修改【%s】条记录成功！" % len(find_data))

# 查
def find(database, sql):
    sql_list = sql.split()
    database = condition(database, sql_list) # 先根据查询条件过滤
    title = ['staff_id','name','age','phone','dept','enroll_date']
    # print(sql_list)
    field_list = sql_list[1].split(",")
    # print(field_list)
    result_list = [] # 保存数据的查询结果
    title_index = [] # 保存要查询出来的列的索引值
    if field_list[0] == '*':
        field_list = title
        result_list = database
    else:
        for field in field_list:
            if field in title:
                title_index.append(title.index(field))
            else:
                exit("要查询的field不存在!")
        # 将查询结果中对应的field写入到result_list中
        for i in range(len(database)):
            result_list.append([])
            for j in range(len(database[i])):
                if j  in title_index:
                    result_list[i].append(database[i][j])
    if len(result_list) < 1:
        print("没有查到对应记录!")
    else:
        print(' '.join(field_list))
        for result in result_list:
            print(' '.join(result))
        print("共查询到【%s】条记录" % len(result_list))


# 主方法
def main():
    database = get_info()
    while True:
        sql = input("Pls. insert your operation sql: ").strip()

        if sql.upper() == 'Q': exit(0)
        if sql.startswith('find'):
            find(database, sql)
        elif sql.startswith('add'):
            add(database, sql)
        elif sql.startswith('del'):
            delete(database, sql)
        elif sql.startswith('update'):
            update(database, sql)
        else:
            print("Error!")
            print(useage)
            break



if __name__ == "__main__":
    while True:
        main()
