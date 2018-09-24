#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/23 6:27

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

def get_level(menu):
    while True:
        if len(menu) == 0: print("The end level !")  # 判断当前菜单下是否有子菜单
        for key in menu:
            print(key)
        choise = input('Pls. insert your choise:("Q" for exit,"B" for back.) ').strip()
        if choise.upper() == "Q": exit("Exit !")
        elif choise.upper() == "B": break  # 最顶层菜单输入B则直接退出程序
        elif choise not in menu:
            print("Wrong input,try again...")
            continue
        else:
            get_level(menu[choise])

get_level(menu)