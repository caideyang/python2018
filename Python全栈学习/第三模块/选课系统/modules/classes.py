#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 21:59

# 班级类
class Classes:

    def __init__(self, name, course_obj):
        self.name = name
        self.course_obj = course_obj
        self.course_student = []  # 该门课程学生列表 ["李同学"，"王同学"]
        self.course_score = {} #该门课程对应的学生成绩字典 {"李同学":85,"王同学":90}


if __name__ == "__main__":
    pass