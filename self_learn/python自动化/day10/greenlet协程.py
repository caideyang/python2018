#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/25 6:57

from greenlet import  greenlet

def test1():
    print("test1,step1 ") #第一步执行
    gr2.switch() #切换到gr2 #第二步执行
    print("test1,step2 ")  #第五步执行
    gr2.switch()           #第六步执行
def test2():
    print("test2 step1")   #第三步执行
    gr1.switch()#切换到gr1  #第四步执行
    print("test2 step2")    #第七步执行

if __name__ == "__main__":
    gr1 = greenlet(test1)#启动一个协程
    gr2 = greenlet(test2)#启动一个协程
    gr1.switch() #先执行gr1  #第0步执行