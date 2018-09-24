#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/20 14:56


class A(object):
    pass

class B(A):
    pass

print(issubclass(B, A)) # True
b = B()
print(isinstance(b, A)) # True
print(isinstance(b, B)) # True


if __name__ == "__main__":
    pass