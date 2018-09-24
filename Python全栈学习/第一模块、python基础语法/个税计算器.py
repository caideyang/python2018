#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/31 16:10

while True:
    salary = int(input("工资： ").strip())
    fee = int(input("五险一金总额: ").strip())
    tax = 0
    if salary - 5000 - fee <= 3000:
        tax += (salary - 5000 - fee) * 0.03
    elif salary - 5000 - 3000 - fee <= 12000:
        tax += 3000 * 0.03 + (salary - 8000 - fee) * 0.1
    else:
        pass
    total = salary - fee - tax
    print("纳税 %s" % tax)
    print("到手工资: %s" % total)
