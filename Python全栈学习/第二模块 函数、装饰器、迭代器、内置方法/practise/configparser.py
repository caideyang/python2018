#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/9 7:36

import configparser

config = configparser.ConfigParser()
#
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
#
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
#
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)

# with open('example.ini','r') as configfile:
#     config.read()
config.read_file('example.ini')

# config = configparser.RawConfigParser()
# config.read("example.ini"


if __name__ == "__main__":
    pass