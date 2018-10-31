#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/10/30 14:43

from django.shortcuts import render

# Create your views here.

def index(request):

    import datetime
    now=datetime.datetime.now()
    ctime=now.strftime("%Y-%m-%d %X")

    return render(request,"index.html",{"ctime":ctime})