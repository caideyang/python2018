#!_*_coding:utf-8_*_
#__author__:"Alex Li"

'''
main program handle module , handle all the user interaction stuff

'''

from core import auth
from core import accounts
from core import logger
from core import accounts
from core import transaction
from core.auth import login_required
import time

#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')


#temp account db ,only saves the db in memory
user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None

}

@login_required
def account_info(acc_data):

    account_data = accounts.load_current_balance(acc_data['account_id'])
    msg = """
    当前账号: %s
    最高额度：%s
    可用额度：%s
    注册时间：%s
    到期时间：%s
    账户状态：%s
    """ % ( account_data['id'],
            account_data['credit'],
            account_data['balance'],
            account_data['enroll_date'],
            account_data['expire_date'],
            "正常" if account_data['status']==0 else "冻结" )
    print(msg )

@login_required
def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    #for k,v in account_data.items():
    #    print(k,v )
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) >0 and repay_amount.isdigit():
            print('ddd 00')
            new_balance = transaction.make_transaction(trans_logger,account_data,'repay', repay_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)

        if repay_amount == 'b':
            back_flag = True

@login_required
def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance= ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' %(account_data['credit'],account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) >0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger,account_data,'withdraw', withdraw_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' %(new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)

        if withdraw_amount == 'b':
            back_flag = True

@login_required
def transfer(acc_data):
    account_data = accounts.load_current_balance(acc_data['account_id'])
    current_balance = ''' --------- BALANCE INFO --------
            Credit :    %s
            Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        transfer_amount = input("\033[33;1mInput transfer amount:\033[0m").strip()
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'transfer', transfer_amount)
            if new_balance:
                print('''\033[42;1mNew Balance:%s\033[0m''' % (new_balance['balance']))

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % transfer_amount)

        if transfer_amount == 'b':
            back_flag = True


@login_required
def pay_check(acc_data):
    account_id = acc_data['account_id']
    import datetime
    import os
    current_month = datetime.datetime.now().strftime('%Y-%m')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    transaction_log_file = os.path.join(base_dir,"log\\transactions.log")
    print(transaction_log_file)
    trans_logs = []
    with open(transaction_log_file,'r') as f:
        for log in f:
            if log.startswith(current_month) and  "account:%s " %account_id in log:
                trans_logs.append(log.strip())
                print(log)


def logout(acc_data):

    account = acc_data['account_id']
    user_data['account_id'] = None
    user_data['is_authenticated'] = False
    user_data['account_data'] = None
    print("账户退出成功！")
    access_logger.info("account [%s] logout successfully!" % account)
    acc_data = auth.acc_login(user_data, access_logger)
@login_required
def interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- Oldboy Bank ---------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # print('accdata',acc_data)
            #acc_data['is_authenticated'] = False
            menu_dic[user_option](acc_data)

        else:
            print("\033[31;1mOption does not exist!\033[0m")
def run():
    '''
    this function will be called right a way when the program started, here handles the user interaction stuff
    :return:
    '''
    print(" ------- Oldboy Bank ---------")
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)