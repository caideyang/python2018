#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 22:04

# 学校类
from conf import settings
from modules.classes import Classes
from modules.teacher import Teacher
from modules.student import Student
from modules.course import Course


class School:

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course = {}  # {课程名：课程实例}
        self.teacher = {}  # {老师名：老师实例}
        self.classes = {}  # {班级名：班级实例}
        self.student = {}  # {学生名：学生实例}
        self.classes_to_teacher = {}  # 无用
        self.classes_to_course = {}   # 无用
        self.classes_to_student = {}  # 无用
        self.class_to_socre = {}      # 无用

    def create_classes(self, classes_name, course_obj):
        classes_obj = Classes(classes_name, course_obj)  # 班级的实例
        self.classes[classes_name] = classes_obj  # 将班级实例放入班级的字典


    def create_course(self, name, period, price):  # 创建课程
        course_obj = Course(name, period, price)
        self.course[name] = course_obj


    def create_teacher(self, teacher_name, teacher_salary, skills,  classes_name, school_name):  # 创建老师
        teacher_obj = Teacher(teacher_name, teacher_salary, skills,  school_name)
        classes_obj = self.classes[classes_name]
        teacher_obj.add_classes(classes_name, classes_obj)  # 将课程关联到老师
        self.teacher[teacher_name] = teacher_obj


    def show_teacher(self):
        for key in self.teacher:
            teacher_obj = self.teacher[key]
            class_list = []
            for key2 in teacher_obj.classes:
                class_list.append(key2)
            print("姓名:%s,薪资:%s,授课班级:%s" % (teacher_obj.name, teacher_obj.salary, class_list))



if __name__ == "__main__":
    pass