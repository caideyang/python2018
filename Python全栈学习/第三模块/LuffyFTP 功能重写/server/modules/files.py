#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/14 10:30

# 该类定义好以后未派上用场

class Files():
    def __init__(self, name, size, md5_value, upload_path):
        self. name = name  # 文件名
        self.size = size   # 文件大小(字节）
        self.md5_value = md5_value # 文件的md5校验值
        self.upload_path = upload_path # 服务器存放路径
    def add_seek(self,size):
        self.seek_place += size
        if self.seek_place > self.size:
            self.seek_place = self.sie
            return True   # 当self.seek_place 大于等于文件大小时，表面文件已经传输完成，返回一个状态
if __name__ == "__main__":
    pass