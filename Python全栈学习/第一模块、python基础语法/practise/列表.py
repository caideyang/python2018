#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/24 15:07

# L = [1,2,3,4,5,2,3,4,67,78,2,78,23]
# M = L[L.index(2)+1:]
# L[L.index(2)+1+M.index(2)] = "二"
# print(L)

products = [ ['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799] ]


buy_list = []
while True:
    print("---------商品列表----------")
    for index, product in enumerate(products):
        print(index, product[0], product[1])
    index = input("Pls insert your id(q for exit!): ").strip()
    if index.upper() == "Q":
        if len(buy_list) == 0:
            print("什么都没有购买。")
        for index,product in enumerate(buy_list):
            print(index,product[0],product[1])
        break
    elif index.isdigit():
        index = int(index)
        buy_list.append(products[index])
        print("购买%s成功，欢迎再次购买!" %products[index][0])
