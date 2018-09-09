#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/5 11:19
import json
import time

from core import auth
from core import logger
from conf import settings
from core import tools

# access_log = logger.logger('pay_auth')
pay_log = logger.logger('pay')
pay_auth = logger.logger('pay_auth')
# 信用卡认证
def account_auth():
    account_data = None
    retry_count = 0
    print("正在调取银行接口.....")
    while account_data is None and retry_count < 3:
        account = input("银行卡号: ").strip()
        password = input("交易密码: ").strip()
        account_data = auth.acc_auth(account, password, type='atm')
        if account_data :
            print("认证成功")
            pay_auth.info("用户账户 [%s] 通过购物商城验证成功！" % account)
            return account_data
        else:
            print("认证失败,请重试！")
            retry_count += 1
    else:
        print("认证失败次数过多，请稍后再试!")

#更新银行账户
def update_account(account_data):
    data_dir = settings.DATABASE['atm']
    account_file = '%s/%s.json' % (settings.DATABASE['atm'], account_data['id'])
    # print(account_file)
    # print(account_data)
    with open(account_file,'w') as f:
        json.dump(account_data,f)
    print("银行扣款成功！")
    trans_time = tools.get_current_time()
    return account_data['id'], trans_time


# 信用卡付款
def pay(user_data, total_amount):
    # print(user_data, total_amount)
    account_data = account_auth()
    if account_data:
        print("账户可用余额: %s " % account_data['balance'])
        if account_data['balance'] >= total_amount:
            account_data['balance'] -= total_amount
            print("交易正在进行,请耐心等待....")
            time.sleep(2)
            trans_result = update_account(account_data)
            print("支付完成！")
            return  trans_result
        else:
            print("信用卡可用余额不足！")
        print(account_data)
    else:
        print("付款失败")

if __name__ == "__main__":
    pass