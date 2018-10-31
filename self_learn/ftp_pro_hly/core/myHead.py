#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Han Liyue"


def head(action_type, filename=None, file_size=None, file_md5=None):
    # head(dir/put,   )
    head_dic = {
        'action_type':action_type,
        'filename':filename,
        'file_size':file_size,
        'file_md5':file_md5
    }
    return head_dic
# s = head("get")
# print(s)