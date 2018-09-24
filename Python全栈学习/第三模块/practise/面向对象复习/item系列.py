#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/20 15:49

class People(object):
    def __init__(self):
        pass

    def __getitem__(self, item):
        print("执行getitem")
        return self.__dict__.get(item)

    def __setitem__(self, key, value):
        print("执行setitem")
        self.__dict__[key] = value

    def __delitem__(self, key):
        print("执行delitem")
        self.__dict__.pop(key)

    def __setattr__(self, key, value):
        print("执行setattr")
        self.__dict__[key] = value

    def __str__(self):
        return "__str__"

    def __repr__(self):
        return "__repr__"

    def __del__(self):
        print("资源释放")

p1 = People()
p1.name = 'caideyang'  # 触发执行__setattr__
p1['name'] = 'caideyang' # 触发执行 __setitem__
print(p1['name'])   # 触发__getitme__
del p1['name']  # 触发执行 __delitem__
print(p1)   # 触发执行__str__ ,

# print(p1["name"])




if __name__ == "__main__":
    pass