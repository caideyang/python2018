#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/24 17:39

# class People(object):
#     __name = "luffy"
#     __age = 18
#
#
# p1 = People()
# print(p1._People__name, p1._People__age)

class People(object):

   def __init__(self):
       print("__init__")

   def __new__(cls, *args, **kwargs):
       print("__new__")
       return object.__new__(cls, *args, **kwargs)

People()
