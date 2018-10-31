#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/8/5 11:46


# def zaoren():
#     print("造人")
#
# def zhongdi():
#     print("种地")
#
# def outter(fn):
#     def inner():
#         print("浇水")
#         fn()
#         print("完工")
#     return inner
#
# zaoren = outter(zaoren)
# zhongdi = outter(zhongdi)
# zaoren()
# print(zaoren.__name__)
# zhongdi()
# print(zhongdi.__name__)

# def warpper(fn):
#     def inner(*args,**kwargs):
#         print("before")
#         ret = fn(*args,**kwargs)
#         print("after")
#         return ret
#     return inner
#
# @warpper
# def func1():
#     print("hello ?")
#
# @warpper
# def func2(name,age):
#     print("my name is %s ,and age is %s" %(name,age))
#
# func1()
#
# func2("caideyang",30)
#
