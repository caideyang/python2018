#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/23 14:29


import paramiko
import threading,os
import json

with open('conf') as f:
    config = json.load(f)
    # print(conf)
for group in config:
    print(group)
group = input("Pls. insert your group:>>>")
print(config[group])
