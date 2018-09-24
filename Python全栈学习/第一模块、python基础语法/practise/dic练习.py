#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/25 14:50


lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
lis[0][1][2]['k1'][0] = 'TT'

print(lis)

li = [1,2,3,'a','b',4,'c']
dic = {}
dic['k1'] = []
dic['k1'].extend(li[1::2])
print(dic)