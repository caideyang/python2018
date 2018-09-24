'''
很明显照着v1这个版本写下去会有大量冗余的代码
'''
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from lib import common
from conf import settings
import random
import pickle
import os
import xlrd
import time
class Subject:
    DB_PATH=settings.QUESTION_PATH
    def __init__(self,type,comment,choice,right_res,score=5):
        self.id=common.create_id()
        self.type=type
        self.comment=comment
        self.choice=choice
        self.right_res=right_res
        self.score=score

    def save(self):
        file_path=r'%s/%s' %(self.DB_PATH,self.id)
        pickle.dump(self,open(file_path,'wb'))

    @classmethod
    def get_obj_by_id(cls,id):
        file_path=r'%s/%s' %(cls.DB_PATH,id)
        return pickle.load(open(file_path,'rb'))

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


class Customer:
    def __init__(self,name,sex,age,phone):
        self.id=common.create_id()
        self.name=name
        self.sex=sex
        self.age=age
        self.phone=phone




class Record:
    def __init__(self,customer_id,record_id_list,total_score):
        self.id=common.create_id()
        self.customer_id=customer_id
        self.record_id_list=record_id_list
        self.total_score=total_score
        self.sub_time=time.strftime('%Y-%m-%d %X')

class Prize:
    def __init__(self,name):
        self.id=common.create_id()
        self.name=name


class Customer2Prize:
    def __init__(self,customer_id,prize_id):
        self.id=common.create_id()
        self.customer_id=customer_id
        self.prize_id=prize_id






if __name__ == '__main__':

    # Subject.create_from_file(r'/Users/jieli/PycharmProjects/爬虫/t1/AnswerSys/test.xlsx')
    res=Subject.filter_question()
    for i in res:
        print(i)