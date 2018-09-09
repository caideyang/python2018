#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/8 5:47

def get_tax():
    salary = int(input("税前工资：").strip())
    insurance = int(input("五险一金： ").strip() or 0)
    deduction = int(input("专项扣除：").strip() or 0)
    taxable = salary - insurance - deduction - 5000
    if taxable <= 0:
        tax == 0
    elif taxable <= 3000:
        tax = taxable * 0.03
    elif taxable <= 12000:
        tax = taxable * 0.1 - 210
    elif taxable <= 25000:
        tax = taxable * 0.2 - 1410
    elif taxable <= 35000:
        tax = taxable * 0.25 - 2660
    elif taxable <= 55000:
        tax = taxable * 0.3 - 4410
    elif taxable <= 80000:
        tax = taxable * 0.35 - 7160
    else:
        tax = taxable * 0.45 - 15160
    hand_pay = salary - insurance - tax
    print("税前工资 【%s】 税后到手工资 【%s】 元,应纳税 【%s】 元！" % (salary,hand_pay,tax))





if __name__ == "__main__":
    while True:
        get_tax()