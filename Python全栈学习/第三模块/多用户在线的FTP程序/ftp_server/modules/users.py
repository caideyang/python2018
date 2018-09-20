#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 7:16

import  os
from conf import settings

class Users:
    def __init__(self, name, password, quta):
        self.name = name
        self.password = password
        self.quota = quta   # 目录限额
        self.used_space = 0  # 已使用目录大小
        self.avaiable_space = quta  # 目录剩余空间大小
        # self.current_path = os.path.join(settings.UploadsDir, name)  #当前目录
        self.current_path = "%s/%s"  %(settings.Ftp_Base_Dir, name)  #当前目录
        self.upload_files = {} #上传的文件记录 {"文件名"："文件实例"}
        # self.download_files = {} #下载的文件记录 {"文件名"："文件实例"}

    @property
    def space_info(self):
        return self.quota, self.used_space, self.avaiable_space

    # 改变空间信息
    def change_space_size(self, size):
        size = size / ( 1024 * 1024 )
        self.avaiable_space -= size
        self.used_space = self.quota - self.avaiable_space

    def mkdir(self,path):
        pass


if __name__ == "__main__":
    pass