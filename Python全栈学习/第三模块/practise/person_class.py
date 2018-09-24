#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/10 9:37

class Person(object):
    def __init__(self, name, age): # 构造方法，初始化方法
        self.name = name
        self.age = age

    def talk(self):
        print("My name is %s ,and age is %s" %(self.name,self.age))

    def __del__(self):  #析构方法，在实例退出时执行，删除该实例在内存中的数据
        print("This person instance %s is deleted by memory" % self.name)

if __name__ == "__main__":
    p = Person('caideyang',31)
    print(p.age,p.name)
    p.talk()
    print('....................')
    # del p
