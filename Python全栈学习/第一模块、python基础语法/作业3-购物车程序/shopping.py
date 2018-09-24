#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/24 7:22
"""
需求：
1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
7、允许查询之前的消费记录
"""
import  json,datetime


error_info = "输入有误，请核对后再输!"

# 设置字体高亮
def set_color(item):
    return "\033[31m"+str(item)+"\033[1m"


# 保存json数据
def save_datebase(database,file="user_info"):
    with open(file,"w") as f:
        json.dump(database,f)

# 获取json数据
def load_database(file="user_info"):
    with open(file,"r") as f:
        database = json.load(f)
    return database

# 获取实时时间，并格式化
def get_current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 获取账户余额
def get_account_salary(account,database):
    database = database
    return database[account]['salary']

# 账户充值，返回实时金额
def recharge(account,database):
    database = database
    while True:
        salary = input("请输入金额：").strip()
        if salary.isdigit():
            salary = int(salary)
            if salary > 0:
                database[account]['salary'] += salary
                save_datebase(database)
                print('您已成功充值%s元,充值后余额为%s元' %(set_color(salary),set_color(database[account]['salary'])))
                break
        else:
            print(error_info)
            break
    return database
# # 账户扣款
# def set_salary(account,cost):
#     database = load_database()
#     database[account]['salary'] -= cost
#     save_datebase(database)

# 获取历史购物记录
def get_shopping_history(account,database):
    database = database
    records = database[account]["shopping_list"]
    if len(records) > 0:
        for record in records:
            print('您于%s购买了%s件%s,单价%s元，总价%s元' % (
                set_color(record["shopping_time"]), set_color(record["num"]), set_color(record["product"]), set_color(record["singlePrice"]), set_color(record["totalCost"])))
    else:
        print("No records !")

# 增加购物记录
def set_shopping_records(account,shopping_record,database):
    database = database
    database[account]['shopping_list'].append(shopping_record)
    save_datebase(database)

# 购物
def shopping(account,database):
    products = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 100},
        {"name": "游艇", "price": 20000},
        {"name": "美女", "price": 998},
        {"name": "粪叉", "price": 6688},
    ]
    while True:
        print("商品列表".center(50, "-"))
        print("编号", "名称".ljust(30, " "), "价格".ljust(10, " "))
        for id in enumerate(products):
            print(id[0],id[1]['name'].rjust(10," "),str(id[1]['price']).ljust(10," "))
        while True:
            p_id = input("请输入您要选择的产品编号(q退出,h查询购物历史，s获取商品列表,m查询余额,t充值):").strip()
            if p_id.upper() == 'Q': logout(database,account)
            elif p_id.upper() == 'S':break
            elif p_id.upper() == 'H':
                get_shopping_history(account,database)
            elif p_id.upper() == 'T':
                recharge(account,database)
            elif p_id.upper() == 'M':
                account_salary = get_account_salary(account,database)
                print('您的账户余额是%s' % set_color(account_salary))
            elif p_id.upper() == '':
                recharge(account,database)
                print('您的账户余额是%s' % set_color(account_salary))
            elif p_id.isdigit():
                if p_id  in map(str,range(len(products))):
                    p_id = int(p_id)
                    p_name = products[p_id]['name']
                    p_num = input('请输入要购买的商品"%s"的数量:' % p_name).strip()
                    if p_num.isdigit():
                        p_num = int(p_num)
                        if p_num == 0:
                            print("您未购买%s ，请重新选择要购买的商品!" % set_color(p_name))
                            break
                        # 获取账户余额
                        account_salary = get_account_salary(account,database)
                        # 单价&总价
                        singlePrice = products[p_id]['price']
                        totalCost = singlePrice * p_num
                        if totalCost > account_salary:
                            print(set_color('您的账户余额不足，请存入工资！'))
                            print('您的账户余额是%s' % set_color(account_salary))
                            g = input("充值输入t，返回上一级输入b，退出输入q':").strip()
                            if g.upper() == 'Q':
                                logout(database,account)
                            if g.upper() == 'B':
                                break
                            if g.upper() == 'T':
                                database = recharge(account,database)
                        else:
                            # 扣款
                            database[account]['salary'] -= totalCost
                            # 获取购物时间
                            shopping_time = get_current_time()
                            print('您成功购买%s件商品:%s!' % (set_color(p_num), set_color(p_name)))
                            shopping_record = {"product": p_name, "num": p_num, "singlePrice": singlePrice, "totalCost": totalCost, "shopping_time": shopping_time}
                            # 新增购物记录
                            set_shopping_records(account,shopping_record,database)
                else :
                    print(error_info)
                    break
            else:
                print(error_info)
                break

# 登陆后操作
def operation(account,database):
    while True:
        command = input('按h查询购物历史,按s开始购物,按t充值,按q退出:').strip()
        database = database
        if command.upper() == 'H':
            get_shopping_history(account,database)
        elif command.upper() == 'T':
            recharge(account,database)
        elif command.upper() == 'S':
            shopping(account,database)
        elif command.upper() == 'Q':
            logout(database,account)
        else:
            print(error_info)

# 用户登陆
def login():
    database = load_database("user_info")
    # blacklist = load_database('user_lock.json')
    print('欢迎登录购物系统！')
    while True:
        account = input("请输入登陆名：").strip()
        if account.upper() == 'Q':
            logout(database,account)
        #if account in blacklist.keys():
        if database[account]["is_locked"]:
            print("当前用户【%s】已经被锁定" % account)
            continue
        if account not in database.keys():
            print("当前用户【%s】不存在" % account)
            continue
        count = 0
        while count <3:
            pwd = input("请输入登陆密码：").strip()
            if pwd == database[account]['pwd']:
                while True:
                    print("登陆成功！")
                    account_salary = get_account_salary(account,database)
                    if account_salary != 0:
                        print('您的账户余额是%s' % set_color(account_salary))
                    else:
                        print(set_color('您的账户余额不足,请存入工资！'))
                        database = recharge(account, database)
                    operation(account,database)
            else:
                print("密码输入错误，请重新输入！")
                count += 1
                continue
        if count == 3: # 密码输错达到3次，则用户锁定
            database[account]["is_locked"] = True
            # print("当前登陆用户%s被锁定" % set_color(account))
            save_datebase(database)
            exit("密码错误已达上限！！！当前登陆用户%s被锁定" % set_color(account))
# 用户退出，打印用户消费历史，并保存数据
def logout(database,account = None):
    if account != None:
        get_shopping_history(account,database)
        save_datebase(database)
    print("欢迎再次光顾！")
    exit()

if __name__ == "__main__":
    login()





