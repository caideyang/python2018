#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/29 12:01

import  sys
if len(sys.argv) != 4:
    exit("useage:   python %s old_str new_str file_name" %(sys.argv[0]))
old_str = sys.argv[1]
new_str = sys.argv[2]
f = open(sys.argv[-1],'w+',encoding="utf-8")
data = f.read()
data = data.replace(old_str,new_str)
print(data)
f.write(data)
f.close()
