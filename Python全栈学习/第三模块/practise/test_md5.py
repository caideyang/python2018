#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/15 19:46

import hashlib
def get_md5(value):
    m = hashlib.md5()
    m.update(value.encode("utf-8"))
    return m.hexdigest()

print(get_md5("123456"))