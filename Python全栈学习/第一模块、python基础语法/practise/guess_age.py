#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/23 21:47

# rate = 0.0325
# money = 10000
#
# count = 1
# while True:
#     money += money * 0.0325
#     print("第%s年，本息和为: %s" %(count,money))
#     if money >= 20000:
#         break
#     count += 1
# # print(count)
# n = 1
# while n <5 :
#     print("*"*n)
#     n += 1
# while n >0:
#     print("*"*n)
#     n -= 1
#
# basic_salary = 3000
# while True:
#     score = int(input("请输入当月业绩: ").strip())
#     if score < 50000:
#         rate = 0
#     elif score < 100000:
#         rate = 0.03
#     elif score < 150000:
#         rate = 0.05
#     elif score < 250000:
#         rate = 0.08
#     elif score < 350000:
#         rate = 0.1
#     else:
#         rate = 0.15
#     total_salary = basic_salary + score * rate
#     print("当月工资总额：%s" % total_salary)
while True:
    distance = int(input("请输入公司距离: ").strip())
    if distance <= 6:
        single_price = 3
    elif distance <= 12:
        single_price = 4
    elif distance <= 22:
        single_price = 5
    elif distance <= 32:
        single_price = 6
    else:
        if (distance - 32) % 20 == 0:
            single_price = 6 + int((distance - 32) / 20)
        else:
            single_price = 6 + int((distance - 32) / 20) + 1
    print("单程费用%s" %single_price)
    total_cost = 0
    for i in range(40):
        if total_cost < 100:
            total_cost += single_price
        elif total_cost <150:
            total_cost += single_price * 0.8
        else:
            total_cost += single_price * 0.5
        print("第%s程总费用%0.2f" %(i+1,total_cost))








