#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/29 7:13


import  chardet


result = chardet.detect(open("test",'rb').read())
print(result) # {'encoding': 'IBM866', 'confidence': 0.6143757788492946, 'language': 'Russian'}

f = open("test","rb")
content = f.read()
f.close()
print(content)
print(content.decode("gbk")) #解码