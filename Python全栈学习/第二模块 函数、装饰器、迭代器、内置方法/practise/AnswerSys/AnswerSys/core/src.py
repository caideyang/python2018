#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
from core import models_v2
import sys

func_dic={}
def make_route(name):
    def deco(func):
        func_dic[name]=func
    return deco


@make_route('1')
def answer():
    record_list=[]
    questions=models_v2.Subject.filter_question()
    num=1
    for question in questions:
        print('''
        %s%s、%s
        %s
        %s
        %s
        %s
        ''' %(question.type,num,question.comment,question.choice[0],
              question.choice[1],question.choice[2],question.choice[3]))

        user_choice=set(input('选项: ').strip().upper())
        score=5 if user_choice == question.right_res else 0
        record=(question.id,user_choice,score)
        record_list.append(record)
        num+=1
    choice=input('提交(Y/N)? ').strip()
    if choice == "Y" or choice == "y":
        commit(record_list)

def commit(record_list):
    '''生成客户对象,生成答题记录'''
    print('\033[45m我们将会根据您提供的信息通知您是否中奖!!!\033[0m')
    while True:
        name=input('姓名: ')
        sex=input('性别: ')
        age=input('年龄: ')
        phone=input('手机号: ')
        record=models_v2.Record.get_obj_by_phone(phone)
        if record:
            print('该手机号已经被注册')
            return
        if all([name,sex,age,phone]):
            break
        else:
            print('所有信息不能为空')
    obj1=models_v2.Customer(name,sex,age,phone) #创建客户
    obj1.save()


    total_score=sum(record[2] for record in record_list)
    obj2=models_v2.Record(obj1.id,record_list,total_score) #创建客户的答题记录
    obj2.save()


@make_route('2')
def search():
    while True:
        phone=input('输入手机号查询答题结果>>: ').strip()
        if phone:break
    record=models_v2.Record.get_obj_by_phone(phone)
    if not record:
        print('您的答题记录不存在')
        return
    total_score=record.total_score
    customer=models_v2.Customer.get_obj_by_id(record.customer_id)
    customer_name=customer.name
    show_str='您好%s 您的总成绩为:%s' %(customer_name,total_score)
    print(show_str.center(80,'='))
    num=1
    for record in record.record_list:
        question=models_v2.Subject.get_obj_by_id(record[0])
        print('''
        %s%s、%s(%s) 正确答案(%s) 得分:%s
        %s
        %s
        %s
        %s
        ''' %(question.type,num,question.comment,''.join(record[1]),
              ''.join(question.right_res),record[2],question.choice[0],
              question.choice[1],question.choice[2],question.choice[3]))

        num+=1

@make_route('3')
def draw_prize():
    while True:
        phone=input('输入手机号开始抽奖>>: ').strip()
        if phone:break

    record=models_v2.Record.get_obj_by_phone(phone)
    total_score=record.total_score
    customer_id=record.customer_id

    prize_record=models_v2.Customer2Prize.get_obj_by_customer_id(customer_id)
    if prize_record:
        print('您已经抽过奖啦,年亲人不要这么贪心,迟早要遭报应的')
        return

    if total_score < 5:
        print('恭喜您获得笨蛋鼓励奖:xxx视频一套')
        print('视频链接:http://www.xxxx.com')
    else:
        prize_name=models_v2.Customer2Prize.draw_prize(customer_id)
        print('恭喜您中奖:%s' %prize_name)


@make_route('4')
def quit():
    sys.exit()


def run():
    msg='''
    1 答题
    2 查看
    3 抽奖
    4 退出
    '''
    print(msg)
    while True:
        choice=input('>>: ').strip()
        if choice == '5':break
        if choice not in func_dic:continue
        func_dic[choice]()





