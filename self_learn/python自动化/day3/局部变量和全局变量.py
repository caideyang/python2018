#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/8/4 11:02

stu_list = ["caideyang","chengwanqing"]

def add_student(stu_list,*args):
    print("修改前stu_list列表值为%s" %stu_list)
    if len(args) > 0:
        for stu in args:
            stu_list.append(stu)
    print("修改后stu_list列表值为%s" %stu_list)


add_student(stu_list,"cwq","程婉晴")
print("当前stu_list列表值为%s" %stu_list)