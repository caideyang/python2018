#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/13 6:54

class Student(object):
    count = 0
    def __init__(self, name, age):
        Student.count += 1
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls):
        print("当前创建了 %s 个Student对象" % cls.count)

if __name__ == "__main__":
    s1 = Student('cdy',31)
    s2 = Student('cdy',31)
    s3 = Student('cdy',31)
    s4 = Student('cdy',31)
    s5 = Student('cdy',31)
    s6 = Student('cdy',31)
    Student.get_count()