#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/22 9:38


import optparse
import pickle
from socket import *


class FTPClient(object):
    """ftp客户端"""

    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="ftp server ip_addr")
        parser.add_option("-P", "--prot", type="int", dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="username")
        parser.add_option("-p", "--password", dest="password", help="password")
        self.options, self.args = parser.parse_args()
        print(self.options, self.args)
        self.client = socket(AF_INET, SOCK_STREAM)
        self.verify_data()
        self.interactive()

    def verify_data(self):
        """查看传入的参数是否正确"""
        if not self.options.server or not self.options.port:
            exit("Invalid options...")

    def useage(self):
        print("Usage: python %s  -h" % (__file__))

    def interactive(self):
        # if self.options['server'] and self.options['port']:
        try:
            self.client.connect((self.options.server, self.options.port))
            self.auth()
        except:
            self.useage()

    def auth(self):
        count = 0
        while count < 3:
            username = self.options.username or input("username:").strip()
            password = self.options.password or input("password: ").strip()
            count += 1
            data = {'username': username, 'password': password, 'action_type': 'auth'}
            self.client.send(pickle.dumps(data))


if __name__ == "__main__":
    client = FTPClient()