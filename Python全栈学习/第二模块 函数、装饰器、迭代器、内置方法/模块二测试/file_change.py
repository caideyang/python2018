#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/9 22:13

with open('02','r',encoding='utf-8') as f:
    data = f.readlines()
with open('02.bak','w',encoding='utf-8') as f:
    data[2] = data[2].replace('不要回答','绝对不能回复')
    data.pop()
    for line in data:
        f.write(line)

if __name__ == "__main__":
    pass