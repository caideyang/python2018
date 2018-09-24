#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/25 4:34
import json
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]
database = {"caideyang":{"passwd":"123456","salary":1000,"is_locked":False,"shopping_list":[{"product": "电脑", "num": 1, "singlePrice": 1999, "totalCost": 1999, "shopping_time": "2018-08-25 04:45:40"}]},
            "deyangcai":{"passwd":"111111","salary":1000,"is_locked":False,"shopping_list":[]},
            "cdy":{"passwd":"112233","salary":1000,"is_locked":True,"shopping_list":[]},
            }
#读取数据
def get_database(file="user_info"):
    with open(file,'r') as f:
        database = json.load(f)
    return database

#保存数据
def save_database(database,file="user_info"):
    with open(file,'w') as f:
        json.dump(database,f)


#登陆
def login():
    pass
if __name__ == "__main__":
    print(get_database())
    # login()