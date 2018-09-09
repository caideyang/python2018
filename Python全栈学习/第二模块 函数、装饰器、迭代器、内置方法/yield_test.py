#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/9 17:37

def range2(n):
    count = 0
    while count < n:
        print("count: %s" % count)
        count += 1
        yield count

new_range = range2(10)
print(type(new_range))
#每当调用一次next的时候，执行一次range2函数的while循环,然后count加1，并将count的结果存到生成器中
t1 = next(new_range)
new_range.__next__()  #等价于next(new_range)
print(t1)


if __name__ == "__main__":
    pass