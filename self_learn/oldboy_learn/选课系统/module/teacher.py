#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 22:03

# 老师类
class teacher:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.classes = {}  # 一个老师可以对应多个班级

    def teacher_add_classes(self, classes_id, classes):
        self.classes[classes_id] = classes  # {班id:班级实例}


if __name__ == "__main__":
    pass