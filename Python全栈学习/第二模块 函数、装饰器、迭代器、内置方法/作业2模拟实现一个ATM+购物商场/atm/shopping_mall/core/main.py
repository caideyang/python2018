#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/4 16:21

import json

from core import auth
from core import logger
from core.auth import login_required
from conf import settings
from core import tools
from core import pay

user_data = {
    'account': None,
    'is_authenticated': False,
    'shopping_cart': None,
    'shopping_record': None
    }
#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')
#pay_logger
pay_log = logger.logger('pay')

@login_required
def shopping(user_data):
    """
    选购商品
    :param user_data:
    :return:
    """
    products = settings.products
    # print(user_data['shopping_cart'])
    print("商品列表： ")
    for item in products:
        print(item,products[item])
    while True:
        choise = input("请输入商品编号(b-退出，c-查看购物车): ").strip()
        if choise == 'b': break
        elif choise == 'c':
            checkout(user_data)
            break
        else:
            product = products[choise]['name']
            add_time = tools.get_current_time()
            # print(user_data['shopping_cart'])
            if product in user_data['shopping_cart']:
                num = int(input("请输入购买数量: ").strip())
                new_num = num + user_data['shopping_cart'][product]['num']
            else:
                user_data['shopping_cart'][product] = {}
                num = int(input("请输入购买数量: ").strip())
                new_num = num
            singlePrice = products[choise]['price']
            totalCost = singlePrice * new_num
            user_data['shopping_cart'][product]['product'] = product
            user_data['shopping_cart'][product]['time'] = add_time
            user_data['shopping_cart'][product]['num'] = new_num
            user_data['shopping_cart'][product]['singlePrice'] = singlePrice
            user_data['shopping_cart'][product]['totalCost'] = totalCost
        # print(user_data['shopping_cart'][product])
            trans_logger.info("用户 [%s] 加入购物车 [%s] 件[ %s ] 商品." %(user_data['account'],num,product))



@login_required
def checkout(user_data):
    """
    结账
    :param user_data:
    :return:
    """
    cart_msg = "名称：%s  数量：%s  单价：%s 总价：%s  加入时间: %s"
    # print(user_data)
    print("购物车列表")
    print("--------------------------------------------------------------------------")
    if len(user_data['shopping_cart']) == 0:
        print("购物车内暂无任何商品")
        return
    for key in user_data['shopping_cart']:
        product = key
        num = user_data['shopping_cart'][key]['num']
        singlePrice = user_data['shopping_cart'][key]['singlePrice']
        totalCost = user_data['shopping_cart'][key]['totalCost']
        add_time = user_data['shopping_cart'][key]['time']
        print(cart_msg % (product, num, singlePrice, totalCost, add_time))
    key_list = []
    pay_list = []
    total_amount = 0
    while True:
        p = input("请输入准备付款的商品(p-结账，b-退出) ：").strip()
        if p == 'p':
            print("结账")
            if total_amount == 0 :
                print("没有需要付款的商品！")
            else:
                trans_result = pay.pay(user_data,total_amount)
                if trans_result:
                    import random
                    pay_account ,trans_time = trans_result
                    serial_number = ''.join(random.sample('01234567890123456789',12))
                    trans_logger.info("用户 [%s] 消费 [%s] 元购买 %s,交易流水号[%s]" % (user_data['account'], total_amount, key_list, serial_number ))
                    pay_log.info("account:%s   action:consume    amount:%s   interest:0.0(备注：通过购物商城消费 [%s] 元,交易流水号 [%s] !)" %(pay_account, total_amount, total_amount, serial_number))
                    # print(pay_list)
                    for trans in pay_list:
                        trans['time'] = trans_time
                        trans['pay_account'] = pay_account
                        trans['serial_number'] = serial_number
                        user_data['shopping_record'].append(trans)
                    pay_list = []
                    for k in key_list:
                        del(user_data['shopping_cart'][k])
                    key_list = []
                    # print("支付完成")

        elif p == 'b':
            break
        elif p in user_data['shopping_cart'] :
            if user_data['shopping_cart'][p] not in pay_list:
                key_list.append(p)
                pay_list.append(user_data['shopping_cart'][p])
                print("添加成功！")
                total_amount += user_data['shopping_cart'][p]['totalCost']
            else:
                print("已添加")
        else:
            print("该商品在购物车内不存在！")



@login_required
def show_record(user_data):
    # print('+++++++++++++++++++++++')
    shopping_record = user_data['shopping_record']
    # print(shopping_record)
    # print("++++++++++++++++++++++++")
    msg = "商品名：%s 数量：%s 单价：%s  总价：%s  付款账号：%s 交易时间：%s  流水号：%s "
    if len(shopping_record) == 0 :
        print("无购物记录")
        return
    print("最新五条购物记录如下：")
    print("-------------------------------------------------------------------")
    recent_record = shopping_record[-5:]
    recent_record.reverse()
    for record in recent_record:
        # print(record)
        print(msg % (record['product'], record['num'], record['singlePrice'], record['totalCost'], record['pay_account'], record['time'], record['serial_number']))
    # print(user_data['shopping_record'])
@login_required
def logout(user_data):
    data_dir = settings.DATABASE['shopping']
    file_name = '%s/%s.json' % (data_dir, user_data['account'])
    account_data = tools.load_database(file_name)
    account_data['shopping_cart'] = user_data['shopping_cart']
    account_data['shopping_record'] = user_data['shopping_record']
    tools.save_database(account_data,file_name)
    access_logger.info("用户[%s] 退出登陆！" % user_data['account'])
    exit()
    # print(user_data)

@login_required
def interactive(user_data):
    print(user_data)
    menu = u'''
        ------- Oldboy Shopping Mall ---------
        \033[32;1m1.  选购商品
        2.  购物车结账
        3.  查询购买记录
        4.  退出
        \033[0m'''
    menu_dic = {
        '1': shopping,
        '2': checkout,
        '3': show_record,
        '4': logout
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](user_data)

        else:
            print("\033[31;1mOption does not exist!\033[0m")

def run():
    print("------- Oldboy Shopping Mall ---------")
    acc_data = auth.login(user_data, access_logger)
    if user_data['is_authenticated']:
        # user_data['account'] = acc_data['account']
        user_data['shopping_cart']= acc_data['shopping_cart']
        user_data['shopping_record']= acc_data['shopping_record']
        interactive(user_data)