#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/30 17:41


# 获取数据
def get_info(file="user_info"):
    with open(file, 'r', encoding="utf-8") as f:
        database = f.readlines()
    return database


# 提交数据
def update_info(database, file="user_info"):
    with open(file, 'w', encoding="utf-8" ) as f:
        for data in database:
            f.write(data)

# 修改个人信息
def modify_info(database, user_index):
    field = """
    请输入要修改的属性:
    1. passwd
    2. name
    3. telephone
    4. age
    5. job
    """
    print(field)
    user_info = database[user_index].split(",")
    while True:
        choice = input("请输入要修改的属性: ").strip()
        if choice.upper() == 'Q': break
        elif choice.isdigit():
            if int(choice) not in range(1,6):
                print("输入错误！")
            else:
                value = input("请输入新的值： ").strip()
                user_info[int(choice)] = value
                new_user_info = ",".join(user_info)
                database[user_index] = new_user_info
        else:
            print("输入错误！")
    update_info(database)


# 打印信息
def print_info(database, user_index):
    database = get_info()
    msg = """
        name:      %s
        telephone: %s
        age:       %s
        job:       %s
    """
    user_info = database[user_index].split(",")
    print(msg % (user_info[2], user_info[3], user_info[4], user_info[5]))



# 主页
def home(database, user_index):
    msg = """
    ---------------------------------------------------
        1 . 修改个人信息
        2.  打印个人信息
    """
    actions = {"1": modify_info, "2": print_info}
    while True:
        print(msg)
        choice = input("Pls. insert your action number: ").strip()
        if choice.upper() == "Q":
            exit()
        elif choice in actions:
            actions[choice](database,user_index)
        else:
            print("输入有误，请重试！")

# 用户登陆
def login():
    database = get_info()
    count = 0
    while count < 3:
        username = input("Pls. insert your name: ").strip()
        passwd = input("Pls. insert your name: ").strip()
        auth_info = username+","+passwd+","
        # print(auth_info)
        # print(database)
        user_index = None
        for data in database:
            if data.startswith(auth_info):
                user_index = database.index(data)
        if user_index is not None:
            print("登陆成功！")
            home(database,user_index)
        else:
            print("账号或密码错误")
            count += 1
    else:
        exit("账号或密码错误达到3次！")



if __name__ == "__main__":
    login()