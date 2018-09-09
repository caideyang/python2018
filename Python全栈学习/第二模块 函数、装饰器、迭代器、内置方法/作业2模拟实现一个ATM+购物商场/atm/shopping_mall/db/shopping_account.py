#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/4 17:17

import json
if __name__ == "__main__":
    shopping_account = {
        'account': "caideyang",
        'password': "123456",
        'status' : 0,
        'shopping_record': [{"product": "鼠标", "num": 1, "singlePrice": 100, "totalCost": 100, "pay_account":1234,"time": "2018-08-25 20:07:34","serial_number":"123456789012"}],
        'shopping_cart':   {"电脑":{ "product": "电脑","num": 1, "singlePrice": 10000, "totalCost": 10000, "time": "2018-08-25 20:07:34"}},
    }
    with open('caideyang.json','w') as f:
        json.dump(shopping_account,f)