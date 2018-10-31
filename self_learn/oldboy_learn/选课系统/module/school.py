#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 22:04

# 学校类
from config import settings
from module.classes import classes
from module.teacher import teacher
from module.student import student
from module.course import course


class school:

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course = {}  # {课程名：课程实例}
        self.teacher = {}  # {老师名：老师实例}
        self.classes = {}  # {班级名：班级实例}

    def create_classes(self, classes_id, course_obj):
        classes_obj = classes(classes_id, course_obj)  # 班级的实例
        self.classes[classes_id] = classes_obj  # 将班级实例放入班级的字典

    def show_classes(self):  # 显示班级关联课程
        for key in self.classes:
            classes_obj = self.classes[key]
            print("班级:%s,关联课程:%s" % (classes_obj.id, classes_obj.course.name))

    def show_classes_course(self):  # 显示班级课程信息
        for key in self.classes:
            classes_obj = self.classes[key]
            course_obj = classes_obj.course
            print("班级【%s】当前课程信息:\n课程:%s,课程周期:%s,课程价格:%s" % (
            classes_obj.id, course_obj.name, course_obj.period, course_obj.price))

    def create_course(self, name, period, price):  # 创建课程
        course_obj = course(name, period, price)
        self.course[name] = course_obj

    def show_course(self):  # 显示课程信息
        for key in self.course:
            course_obj = self.course[key]
            print("课程:%s,课程周期:%s,课程价格:%s" % (course_obj.name, course_obj.period, course_obj.price))

    def create_teacher(self, teacher_name, teacher_salary, classes_id):  # 创建老师
        teacher_obj = teacher(teacher_name, teacher_salary)
        classes_obj = self.classes[classes_id]
        teacher_obj.teacher_add_classes(classes_id, classes_obj)  # 将课程关联到老师
        self.teacher[teacher_name] = teacher_obj

    def update_teacher(self, teacher_name, classes_id):  # 更新老师的课程信息
        teacher_obj = self.teacher[teacher_name]
        class_obj = self.classes[classes_id]
        teacher_obj.teacher_add_classes(classes_id, class_obj)

    def show_teacher(self):
        for key in self.teacher:
            teacher_obj = self.teacher[key]
            class_list = []
            for key2 in teacher_obj.classes:
                class_list.append(key2)
            print("姓名:%s,薪资:%s,授课班级:%s" % (teacher_obj.name, teacher_obj.salary, class_list))

    def create_student(self, name, age, classes_id):
        student_obj = student(name, age)
        class_obj = self.classes[classes_id]
        class_obj.course_student[name] = student_obj  # 将学生对象以名字为键添加到classes下面的学生信息字典中
        self.classes[classes_id] = class_obj  # 将新的数据更新只self.classes中

    def show_teacher_classesinfo(self, teacher_name):
        # 该老师对应的实例
        teacher_obj = self.teacher[teacher_name]
        # 获取老师授课班级的实例
        for key in teacher_obj.classes:
            class_obj = teacher_obj.classes[key]
            student_list = []
            for key2 in class_obj.course_student:  # 遍历学员信息
                student_list.append(key2)
            print("班级:%s,关联课程%s,学员:%s" % (class_obj.id, class_obj.course.name, student_list))


if __name__ == "__main__":
    pass