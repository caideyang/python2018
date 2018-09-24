#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/9 7:36

import configparser

config = configparser.ConfigParser()
#
# conf["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# conf['bitbucket.org'] = {}
# conf['bitbucket.org']['User'] = 'hg'
# conf['topsecret.server.com'] = {}
#
# topsecret = conf['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# conf['DEFAULT']['ForwardX11'] = 'yes'
#
# with open('example.ini', 'w') as configfile:
#     conf.write(configfile)

# with open('example.ini','r') as configfile:
#     conf.read()
config.read_file('example.ini')

# conf = configparser.RawConfigParser()
# conf.read("example.ini"


if __name__ == "__main__":
    pass