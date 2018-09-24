#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/21 10:46

class Student(object):

    def __call__(self, *args, **kwargs):
        print(self)
        print(args)
        print(kwargs)

if __name__ == "__main__":
    s = Student()
    s("hello", "caideyang", name='caideyang', age='31')  # 调用对象时，执行类的__call__()函数