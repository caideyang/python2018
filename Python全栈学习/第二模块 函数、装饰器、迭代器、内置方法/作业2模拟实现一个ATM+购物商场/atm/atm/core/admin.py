#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/4 10:41

import os
import datetime
import json

from conf import settings
from core import auth
from core import accounts
from core import logger
from core import transaction
from core.auth import login_required

# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# from core import main

#transaction logger
manage_logger = logger.logger('manage')
#access logger
access_logger = logger.logger('access')

conn_params = settings.DATABASE
db_path = '%s/%s' % (conn_params['path'], conn_params['name'])

user_data = {
    'manager':None,
    'is_authenticated':False,

}
def add_account():
    """
    创建账户
    {"balance": 15008.95, "expire_date": "2021-01-01", "enroll_date": "2016-01-02", "credit": 15000, "id": 1234, "status": 0, "pay_day": 22, "password": "abc"}
    :return:
    """
    while True:
        account_data = {}
        account_id = input("请输入账号：").strip()
        account_file = "%s/%s.json" % (db_path, account_id)
        if os.path.isfile(account_file):
            print("当前账号已存在！")
            continue
        else:
            credit = int(input("请输入额度： ").strip())
            enroll_date =  str(datetime.date.today())
            pay_day = int(input("请输入账单日： ").strip())
            from dateutil.relativedelta import relativedelta
            import random
            expire_date = str(datetime.datetime.today() + relativedelta(years=+5))[:10]
            print(enroll_date)
            print(expire_date)
            status = int(input("是否冻结：0-否 1-是").strip())
            password = ''.join(random.sample('0123456789', 6)) #默认密码
            account_data['id'] = account_id
            account_data['credit'] = credit
            account_data['balance'] = credit
            account_data['enroll_date'] = enroll_date
            account_data['expire_date'] = expire_date
            account_data['status'] = status
            account_data['password'] = password
            account_data['pay_day'] = pay_day
            import json
            with open(account_file, 'w') as f:
                json.dump(account_data,f)
                manage_logger.info("账号[%s]创建成功" %account_id)
                print("账号[%s]创建成功，初始密码[%s]" %(account_id,password))
                break

def get_account():
    accounts_list = [account_file.split(".")[0] for account_file in os.listdir(db_path)]
    # print(accounts_list)
    print("当前系统存在的信用卡账户如下：")
    print(accounts_list)
    while True:
        account = input("请输入要查看的信用卡账户详细信息: ").strip()
        if account == 'b':break
        elif account not in accounts_list:
            print("该账户不存在！")
        else:
            account_file = "%s/%s.json" % (db_path, account)
            manage_logger.info("查看账户[%s]信息" % account)
            with open(account_file,'r') as f:
                account_data = json.load(f)
            msg = """
               银行账号: %s
               最高额度：%s
               可用额度：%s
               注册时间：%s
               到期时间：%s
               账户状态：%s
               """ % (account_data['id'],
                      account_data['credit'],
                      account_data['balance'],
                      account_data['enroll_date'],
                      account_data['expire_date'],
                      "正常" if account_data['status'] == 0 else "冻结")
            print(msg)

def change_account():
    while True:
        account_id = input("请输入要查修改的信用卡账户: ").strip()
        if account_id == 'b':
            break
        account_file = "%s/%s.json" % (db_path, account_id)
        if os.path.isfile(account_file):
            with open(account_file, 'r') as f:
                account_data = json.load(f)
            while True:
                msg = """
                    1. 调整额度
                    2. 延长到期时间
                    3. 冻结账户
                    4. 解冻账户
                    5. 保存退出
                    6. 直接退出
                """
                print(msg)
                choise = input("请输入要调整的属性编号：").strip()
                if choise == '5':
                    with open(account_file ,'w') as f:
                        json.dump(account_data,f)
                        manage_logger.info('修改[%s]信息成功！' % account_id)
                    break
                elif choise == '6':
                    break
                elif choise == '1':
                    old_credit = account_data['credit']
                    account_data['credit'] = int(input("请输入新的额度: ").strip())
                    account_data['balance'] += account_data['credit'] - old_credit
                elif  choise == '2':
                    year = int(input("请输入延长的年限：").strip())
                    new_date = account_data['expire_date'].split('-')
                    new_date[0] = str(int(new_date[0]) + year)
                    account_data['expire_date'] = '-'.join(new_date)
                elif choise == '3':
                    account_data['status'] = 1
                elif choise == '4':
                    account_data['status'] == 0
                else:
                    print("输入错误，请重试")

        else:
            print("要修改的账户不存在")


def frozen_account():
    pass

def logout():
    account = user_data['manager']
    user_data['manager'] = None
    user_data['is_authenticated'] = False
    # print("账户退出成功！")
    access_logger.info("manager [%s] logout successfully!" % account)
    exit("账户退出成功!")

def interactive():
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- Oldboy Bank Manager---------
    \033[32;1m1.  添加账户
    2.  查看用户
    3.  调整用户账户信息
    4.  退出
    \033[0m'''
    menu_dic = {
        '1': add_account,
        '2': get_account,
        '3': change_account,
        '4': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # print('accdata',acc_data)
            #acc_data['is_authenticated'] = False
            menu_dic[user_option]()

        else:
            print("\033[31;1mOption does not exist!\033[0m")
def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    print("------- Oldboy Bank Manage---------")
    acc_data = auth.admin_login(user_data,access_logger)
    if user_data['is_authenticated']:
        interactive()







if __name__ == "__main__":
    pass