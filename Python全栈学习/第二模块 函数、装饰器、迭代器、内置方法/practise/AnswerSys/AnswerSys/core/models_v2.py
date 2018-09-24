# import os,sys
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

from lib import common
from conf import settings
import random
import pickle
import os
import xlrd
import time

class Base:
    def save(self):
        file_path=r'%s/%s' %(self.DB_PATH,self.id)
        pickle.dump(self,open(file_path,'wb'))

    @classmethod
    def get_obj_by_id(cls,id):
        file_path=r'%s/%s' %(cls.DB_PATH,id)
        return pickle.load(open(file_path,'rb'))

class Subject(Base):
    DB_PATH=settings.QUESTION_PATH
    def __init__(self,type,comment,choice,right_res,score=5):
        self.id=common.create_id()
        self.type=type
        self.comment=comment
        self.choice=choice
        self.right_res=right_res
        self.score=score


    @classmethod
    def create_from_file(cls,src_file):
        data=xlrd.open_workbook(src_file)
        table=data.sheets()[0]
        subject={
            'type':None,
            'comment':None,
            'choice':[],
            'res':set(),
        }
        for i in range(2,table.nrows):
            row=table.row_values(i)
            if len(subject['choice'])==4:
                obj=cls(
                    subject['type'],
                    subject['comment'],
                    subject['choice'],
                    subject['res']
                )
                obj.save()
                subject={
                    'type':None,
                    'comment':None,
                    'choice':[],
                    'res':set()
                }
            if row[0]:
                subject['type']=row[0]
                subject['comment']=row[1]
            else:
                subject.setdefault('choice').append(row[2])
                if row[3] == 1:
                    res_str=row[2].strip()
                    res=res_str[0].upper()
                    subject['res'].add(res)

        else:
            obj=cls(
                subject['type'],
                subject['comment'],
                subject['choice'],
                subject['res']
            )
            obj.save()

    @classmethod
    def filter_question(cls):
        id_l=os.listdir(settings.QUESTION_PATH)
        r_id_l=random.sample(id_l,3)
        return [cls.get_obj_by_id(id) for id in r_id_l]

    def __str__(self):
        return '<type: %s comment: %s>' %(self.type,self.comment)


class Customer(Base):
    DB_PATH=settings.CUSTOMER_PATH
    def __init__(self,name,sex,age,phone):
        self.id=common.create_id()
        self.name=name
        self.sex=sex
        self.age=age
        self.phone=phone


class Record(Base):
    DB_PATH=settings.RECORD_PATH
    def __init__(self,customer_id,record_list,total_score):
        self.id=common.create_id()
        self.customer_id=customer_id
        self.record_list=record_list
        self.total_score=total_score
        self.sub_time=time.strftime('%Y-%m-%d %X')

    @classmethod
    def get_obj_by_phone(cls,phone):
        records=(cls.get_obj_by_id(id) for id in os.listdir(cls.DB_PATH))
        for record in records:
            customer_obj=Customer.get_obj_by_id(record.customer_id)
            if phone == customer_obj.phone:
                return record


class Prize(Base):
    DB_PATH=settings.PRIZE_PATH
    def __init__(self,name):
        self.id=common.create_id()
        self.name=name

    @classmethod
    def create_prize(cls):
        while True:
            name=input('奖品名: ').strip()
            if not name:continue
            obj=Prize(name)
            obj.save()
            choice=input('继续(Y/N)?: ').strip()
            if choice == 'N' or choice == 'n':
                break

    @classmethod
    def get_obj_by_name(cls,name):
        prizes=(cls.get_obj_by_id(id) for id in os.listdir(cls.DB_PATH))
        for prize in prizes:
            if prize.name == name:
                return prize

    def __str__(self):
        return '<%s>' %self.name

class Customer2Prize(Base):
    DB_PATH=settings.C2P_PATH
    def __init__(self,customer_id,prize_id):
        self.id=common.create_id()
        self.customer_id=customer_id
        self.prize_id=prize_id

    @classmethod
    def get_obj_by_customer_id(cls,customer_id):
        prizes=(cls.get_obj_by_id(id) for id in os.listdir(cls.DB_PATH))
        for prize in prizes:
            if prize.customer_id == customer_id:
                return prize

    @classmethod
    def draw_prize(cls,customer_id):
        '''
        奖品概率:
        0/100 欧洲十国游
        1/100 iphone7 plus
        10/100 mac电脑
        50/100 珍藏版alex写真集一套
        39/100 egon签名一个
        '''
        num=random.randint(1,100)

        if num == 1:
            # 1/100 iphone7 plus
            prize_name='欧洲十国游'

        if num >1 and num <=11:
            # mac电脑
            prize_name='mac电脑'
        if num > 11 and num <=61:
            # 珍藏版alex写真集一套
            prize_name='珍藏版alex写真集一套'
        if num > 61:
            # egon签名一个
            prize_name='egon签名一个'
        prize=Prize.get_obj_by_name(prize_name)
        obj=cls(customer_id,prize.id)
        obj.save()
        return prize_name

if __name__ == '__main__':

    # Subject.create_from_file(r'/Users/jieli/PycharmProjects/爬虫/t1/AnswerSys/test.xlsx')
    # res=Subject.filter_question()
    # for i in res:
    #     print(i)

    Prize.create_prize()