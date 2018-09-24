#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/20 15:23

class People():
    sex = 'male'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_userinfo(self):
        return "name: %s , age: %s " % ( self.name, self.age)

    @classmethod
    def get_sex(cls):
        return cls.sex

    @staticmethod
    def change_sex():
        print("hehehe")

p1 = People('caideyang', 31)
print(hasattr(p1, "name")) # True
print(hasattr(People, "name")) # False
print(hasattr(People, 'sex')) # True
print(hasattr(p1, 'get_userinfo')) # True
print(hasattr(People, 'get_userinfo')) # True
print(hasattr(People, 'get_sex')) # True
print(hasattr(p1, 'get_sex')) # True
print(p1.get_sex()) # male 类方法可以被实例直接调用
print(hasattr(p1, 'change_sex')) #True
p1.change_sex()  # hehehe  静态方法可以被类和实例直接调用

getattr(p1, 'change_sex')() # hehehe
delattr(p1, 'change_sex')
print(p1.__dict__)
if __name__ == "__main__":
    pass