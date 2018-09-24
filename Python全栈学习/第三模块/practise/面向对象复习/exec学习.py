#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/20 18:32
class MyMeta(type):
    def __init__(self, class_name, class_obj, class_dict):
        if not class_name.istitle():
            raise TypeError("类名称首字母必须大写!")
        if "__doc__" not in class_dict or not class_dict['__doc__'].strip():
            raise  TypeError("%s类没有写注释文档，或注释文档为空" % class_name )
        super().__init__(class_name, class_obj, class_dict)
        print(class_dict)
    def __call__(self, *args, **kwargs):
        print("========>")
        print(args)

class Student(object, metaclass=MyMeta):
    """
    aaaaaaaaaaaaaa
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return "name: %s age: %s" %(self.name, self.age)

s = Student('caideyang', 31)
