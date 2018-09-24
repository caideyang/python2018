#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/23 22:28

class MyException(BaseException):
    def __init__(self,msg):
        super().__init__()
        self.msg = msg
    def __repr__(self):
        return  "<%s>" % self.msg

raise MyException("异常测试！")


if __name__ == "__main__":
    pass