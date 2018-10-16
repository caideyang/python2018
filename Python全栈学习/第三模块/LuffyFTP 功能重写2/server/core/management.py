#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/22 9:52

from core import main

class ManagementTool(object):
    """负责对用户输入的指令进行解析并调用相应模块处理"""
    def __init__(self, sys_argv):
        self.sys_argv = sys_argv
        self.varify_argv()
        self.run()

    def varify_argv(self):
        if len(self.sys_argv) < 2:
            print("where is 参数？")
            self.useage()

    def useage(self):
        msg = """
        Useage:
        python %s  start | stop | restart       
        """ % self.sys_argv[0]
        exit(msg)

    def run(self):
        if hasattr(self, self.sys_argv[1]):
            getattr(self, self.sys_argv[1])()
        else:
            print("参数错误！")

    def start(self):
        print("正在启动Ftp Server服务。。。。")
        # ftp_server = main.FTPServer(self)
        ftp_server = main.FTPServer(self)
        ftp_server.run_forever()
    #
    # def stop(self):
    #     self.ftp_server = main.FTPServer(self)
    #     self.ftp_server.stop()
    #
    # def restart(self):
    #     self.ftp_server.restart()
if __name__ == "__main__":
    pass