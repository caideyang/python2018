#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 22:03

# 老师类
class Teacher:

    def __init__(self, name, salary, skills, school_name):
        self.name = name
        self.salary = salary
        self.skills = skills
        self.school_name = school_name
        self.classes = {}  # 一个老师可以对应多个班级

    def add_classes(self, classes_name, classes_obj):
        self.classes[classes_name] = classes_obj  # {班id:班级实例}


if __name__ == "__main__":
    pass