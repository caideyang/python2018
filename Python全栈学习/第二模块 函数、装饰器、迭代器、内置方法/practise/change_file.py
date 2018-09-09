#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/6 15:31


import sys
import os

# print(sys.argv)

error = " USAGE: python change_file.py old_str  new_str  file_name "
if len(sys.argv) != 4:
    exit(error)
if os.path.isfile(sys.argv[3]):
    with open(sys.argv[3],'r',encoding='utf-8') as f:
        data = f.readlines()
    with open(sys.argv[3],'w',encoding='utf-8') as f:
        print(data)
        for line in data:
            new_line = line.replace(sys.argv[1],sys.argv[2])
            # print(new_line)
            f.write(new_line)
    print("替换完成！")
else:
    print("Error: 文件【%s】不存在" % sys.argv[3])