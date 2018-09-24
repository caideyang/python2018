#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/8/27 21:34


"""
知识点：
计算机语言分类：
1.机器语言：二进制01代码，较繁琐，执行效率最高
2.汇编语言：英文缩写的指令，更容易识别，执行效率高
3.高级语言：C  C++ JAVA Python Go PHP等，在运行前后者运行时需要编译，执行效率较低
编译型语言：程序运行前需要先编译成可执行文件(类似与windows的exe文件），执行效率高，跨平台性差，程序变更麻烦
解释型语言：应用程序源码在执行时由相应的解释器进行解释并运行，执行效率低，跨平台性好，变更方便
python数据类型：
int
str
bool
list
tuple
dict
set
python编码格式：
python2 默认ascii ，python默认utf-8
变量命名规范：
1.数字、大小写字母、下划线
2.数字不能放在第一位
3.python关键字不能
"""

"""
7. 列表li = ['alex','egon','yuan','wusir','666']（编程）（3分钟）  
    - 1.把666替换成999
    - 2.获取"yuan"索引
    - 3.假设不知道前面有几个元素，分片得到最后的三个元素
"""
li = ['alex','egon','yuan','wusir','666']
li[-1] = '999'
print(li.index('yuan'))
print(li[-3:])

"""
9. 对字典进行增删改查（编程）（5分钟）

    ```python
    d = {
            "Development":"开发小哥",
            "OP":"运维小哥",
            "Operate":"运营小仙女",
            "UI":"UI小仙女"
        }
    ```
"""
d = {
    "Development": "开发小哥",
    "OP": "运维小哥",
    "Operate": "运营小仙女",
    "UI": "UI小仙女"
}
#查
for key in d:
    print(d[key])
d.pop('UI') #删
d['OP'] = '运维菜鸟' #改
d['HR'] = '人力美女' #增
print(d)

count = 0
for i in range(1,101):
    count += i
print(count)


"""
11. 制作趣味模板程序（编程题）（5分钟）    
  需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实    
  如：敬爱可爱的xxx，最喜欢在xxx地方干xxx  
"""
while True:
    name = input("Your name: ").strip()
    place = input("Place: ").strip()
    hobby = input("hobby: ").strip()

    print("敬爱可爱的%s，最喜欢在%s地方干%s" % (name,place,hobby))














