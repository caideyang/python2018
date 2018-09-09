#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/6 14:33



#
# flag = True
# f = open('test4.txt','w',encoding='utf-8')
# while flag:
#     msg = input("请输入你的名字: ").strip()
#     f.write("您好，%s \n" % msg)
#     f.flush()
#     if msg == 'exit':
#         f.close()
#         flag = False


f = open('test4.txt','r',encoding='utf-8')
data1 = f.readlines()
print("111111111")
print(data1)
f.seek(0)
data2 = f.read()
print('2222222222')
f.seek(0)
data3 = f.readline()
# print(data1,data2,data3)

print(data2)
print('3333333333')
print(data3)