#encoding:utf-8
import paramiko

#导入私钥文件，秘钥可以使用linux系统生成的
private_key = paramiko.RSAKey.from_private_key_file("id_rsa")

ssh = paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器,配置需要连接的服务器IP、端口、用户名、密码
ssh.connect(hostname='192.168.56.12',port=22,username='root',pkey=private_key)
while True:
    command = input(">>>").strip()
    if command == 'exit':
        break
    #执行命令
    stdin,stdout,stderr = ssh.exec_command(command)
    # 获取命令结果
    result = stdout.read().decode()
    print(result)
#关闭连接
ssh.close()