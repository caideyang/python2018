from certForDogs import CertForDog
import os


if __name__ == "__main__":
    print("Excel文件需放置到【D:\mydogs】路径下面")
    file_name = input("请输入excel文件名字：")
    dir_name = file_name.split(".")[0]
    # 创建一个对象，导入狗狗信息D:\cert_dog.xlsx  ，导出位置D:\mydogs
    cert = CertForDog('D:\\mydogs\\data\\%s' %file_name, 'D:\\mydogs\\data\\%s' %dir_name)
    # 创建导出位置
    cert.crateDir()
    # 获取狗狗信息，参数0 是获取第一个sheet的值
    dogs_info = cert.getDogInfo(0)
    #     print(dogs_info)
    # 根据模板，创建证书，模板位置：'D:\template'
    cert.createCert('D:\\mydogs\\template', dogs_info)
    cert.createCertDetail('D:\\mydogs\\template', dogs_info)