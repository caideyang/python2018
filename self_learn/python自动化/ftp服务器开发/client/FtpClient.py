#encoding:utf-8

import socket
import os,json
class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        msg = """
        ls
        pwd
        cd ../..
        get filename
        put filename
        """
        print(msg)
    def connect(self,ip,port):
        self.client.connect((ip,port))
    def authenticate(self):
        self.username = input("username>>>")
        self.password = input("password>>>")
        self.auth = {"username":self.username,"password":self.password}
        self.client.send(json.dumps(self.auth).encode())
        self.result = self.client.recv(1024).strip()
        if self.result.decode() != 'OK' :
            exit("Authenticated Failed !")
        else:
            print("认证成功！")
    def interactive(self):
        self.authenticate() #认证
        while True:
            cmd = input(">>>").strip() #输入要进行操作的指令和对应的文件
            if len(cmd) == 0 : continue #如果输入为空，则重写输入
            cmd_str = cmd.split()[0] #获取操作指令如get/put/ls/pwd等
            if hasattr(self,"cmd_%s" % cmd_str): #使用hasattr检测类是否有这个方法
                func = getattr(self,"cmd_%s" % cmd_str) #使用getattr反射到相应的方法
                func(cmd) #调用对应的方法
            else:
                self.help()

    def cmd_ls(self):
        pass
    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):  #判断文件是否存在
                filesize = os.stat(filename).st_size #获取文件的大小
                msg_dic = {
                    "action":"put",
                    "filename":filename,
                    "filesize":filesize,
                    "overridden": True
                }  #以字典的形式存储需上传的文件信息
                self.client.send(json.dumps(msg_dic).encode()) #将字典转换为json字符串，并发送给server端
                print("Send ",json.dumps(msg_dic).encode())
                server_response = self.client.recv(1024)  #等待服务端确认，防止粘包发生
                f = open(filename,'rb')
                sendsize = 0
                for line in f :
                    self.client.send(line)
                else:
                    print("Send Successfully !")

            else:
                print("%s is not exist !" % filename)

if __name__ == "__main__":
    ftp_client = FtpClient()
    ftp_client.connect("localhost",9999)
    ftp_client.interactive()
