#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/8 22:15



# data = shelve.open('test_shelve.db')
# print(data)
#
# if __name__ == "__main__":
#     pass

import shelve
f = shelve.open("test_shelve")
# # names = ["alex", "rain", "test",'deyang']
# info = {'name':'alex','age':22}
# # f['names'] = names
# f['info'] = info
# f.close()
del f['name']
for key in f:
    print(key,f[key])

f.close()