#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/7 13:55



import re
#
# data = open('log_test.log','r')
# for line in data:
#     if re.match('INFO',line):  #match从开头开始匹配
#         print(line)

# str = """
# caixiansheng   18    35000   13911234345
# shixiaodong    31    15000   13266661111
# sunningxuan    20    10000   13433322222
# siyang         30    20000   13344466663
# """
# res = re.findall('([a-z]+)\W+(\d+)\W+(\d{5})\W+(\d{11})\W*', str)
# print(res)


# 手机号匹配
# patten = re.compile('1(3|5|7|8)\d{9}')
#
# while True:
#     tel = input("Tel: ").strip()
#     if patten.fullmatch(tel):
#         print("%s 是合法的手机号!" % tel )
#     else:
#         print("非合法手机号！")


#验证邮箱
# pattern = re.compile('\w+@\w+\.(com|cn|net|org)')
# while True:
#     tel = input("Tel: ").strip()
#     if pattern.fullmatch(tel):
#         print("%s 是合法的email!" % tel )
#     else:
#         print("非合法email！")

f = open('tel','r')
res = []
for line in f:
    if re.match(".+\d{11}$",line):
        tel = re.search("\d{11}$",line).group()
        res.append(tel)
print(res)