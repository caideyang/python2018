#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/29 10:26


# f = open('test','rb')
# data = f.read()
# print(data)
# print(data.decode('utf-8'))
# f.close()

# encode ：编码
# decode ：解码
# f = open('test','ab')
# f.write(b"\nasdfg")
# f.close()

# f = open('test.txt','rb')
# print(f.read().decode())
# f.close()

# import chardet
# f = open('test.txt','rb')
# print(chardet.detect(f.read()))
# f.close()

#
# f = open('test.txt','r+',encoding='utf-8')
# # f.write("\n岳妮妮 	深圳	177	54	18835324553")
# # data = f.read()
# # print(data)
# import time
# while True:
#     f.write("\n哈哈哈哈哈7")
#     f.flush()
#     time.sleep(1)
# f.close()


f = open("test.txt",'r',encoding='utf-8')
f.seek(3)
print(f.readline())


