#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/29 20:11

import os

# old_file = "test2"
# new_file = "%s.new" % old_file
# old_str = "abc"
# new_str = "ABC"
# f = open(old_file,'r',encoding='utf-8')
# f_new = open(new_file,'w',encoding='utf-8')
# for line in f:
#     if old_str in line:
#         line = line.replace(old_str,new_str)
#     f_new.write(line)
# f.close()
# f_new.close()
# os.rename(new_file,old_file)

f = open("test2",'r',encoding="utf-8")
data = f.readlines()
f.close()
f = open("test2",'w',encoding="utf-8")
count = 0
for line in data:
    if "abc" in line:
        count += 1
        line = line.replace("abc","ABC")
    f.write(line)
f.close()
print(count)
