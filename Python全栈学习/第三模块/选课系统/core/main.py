#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 22:41

import os
import sys
from controller.student_manage import StudentManage
from controller.teacher_manage import TeacherManage
from controller.school_manage import SchoolManage

def run():
    msg = """
        ---------欢迎使用选课系统-------------------
        1 学员管理系统
        2 讲师管理系统
        3 学校管理系统
        q 退出
        """
    func_dict = {
        "1": StudentManage,
        "2": TeacherManage,
        "3": SchoolManage
    }
    while True:
        print(msg)
        choise = input("请选择(q-退出): ").strip()
        if choise in func_dict:
            func_dict[choise]()
        elif choise == 'q':
            exit(0)
        else:
            print("输入无效！")

if __name__ == "__main__":
    pass