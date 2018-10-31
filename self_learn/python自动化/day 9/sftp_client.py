#encoding:utf-8

import paramiko
#导入私钥文件，秘钥可以使用linux系统生成的
private_key = paramiko.RSAKey.from_private_key_file("id_rsa")
transport = paramiko.Transport(('192.168.56.12',22))
# transport.connect(username='root',password='passwd')
transport.connect(username='root',pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get('/root/cobbler.ks','fromlinux_cobbler.ks')

transport.close()