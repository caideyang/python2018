#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/17 10:35


class Bar:
    __N = 100
    def __init__(self, name, age):
        self.__name = name   # 变形为self._Bar__name = name
        self.__age = age
    def __set_age(self):
        self.__age += 1

b = Bar('caideyang', 31)
print(Bar.__dict__)
print(b.__dict__)  # {'_Bar__name': 'caideyang', '_Bar__age': 31}
# print(b.__name)   #报错
print(b._Bar__name) # caideyang
print(b._Bar__N)   # 100  类的属性也可以通过这种方式访问