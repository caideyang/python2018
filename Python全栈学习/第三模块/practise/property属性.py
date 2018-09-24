#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/17 11:04

# class People():
#     def __init__(self, name, age, weight, height):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.height = height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
# if __name__ == "__main__":
#     p = People('caideyang', 31, 70, 1.70)
#     print(p.bmi)

class Foo:
    def __init__(self, val):
        self.__name = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_val):
        if not isinstance(new_val, str):
            raise TypeError("%s must be str value" % new_val)
        self.__name = new_val

    @name.deleter
    def name(self):
        raise TypeError("Can't delete ")

f = Foo('caideyang')
print(f.name)
# f.name=10 #抛出异常'TypeError: 10 must be str'
f.name = 'deyangcai'
del f.name  # TypeError: Can't delete
