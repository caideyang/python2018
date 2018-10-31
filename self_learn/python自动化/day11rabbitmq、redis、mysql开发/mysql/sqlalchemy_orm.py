#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/31 15:53


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Enum,DATE
from sqlalchemy.orm import sessionmaker
import random

engine = create_engine(
    "mysql+pymysql://cdy:passwd@192.168.56.11/mydb?charset=utf8", #数据库连接
    encoding="utf-8", #编码格式
    echo=False  #运行输出日志,True输出，False不输出
)
Base = declarative_base() #生成orm基类
class User(Base):
    __tablename__ = "user" #b表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    passwd = Column(String(64))
    def __repr__(self):
        return "<%s,%s,%s>" %(self.id,self.name,self.passwd)

class School(Base):
    __tablename__ = "school" #b表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    addr = Column(String(200))

class Student(Base):
    __tablename__ = "student" #学生表
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    register_date = Column(DATE,nullable=False)
    gender = Column(Enum("M","F"),nullable=False)

Base.metadata.create_all(engine) #创建表结构,如果不存在则创建，存在则不创建

Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class
Session = Session_class()

# #新增
# user_obj = User(name="jack",passwd="jack1234")  #生成你要创建的数据对象
# school_obj = School(name="郑州大学",addr="河南省郑州市") #生成你要创建的数据对象
# print(user_obj.name,user_obj.id)
# print(school_obj.name,school_obj.addr)
# Session.add(user_obj)
# Session.add(school_obj)
# Session.commit() #统一提交，创建数据
# #查询
# res = Session.query(User).filter_by(name="alex").all() #查询，all()是把所有符合查询条件的数据取出来放到列表  [<1,alex,alex1234>]
# # res = Session.query(User).filter_by(name="alex").first() #查询，first()是把所有符合查询条件的数据取第一条#<1,alex,alex1234>
# # res = Session.query(User).filter(User.id > 1).all() #查询，id>1 的数据，过滤使用filter(),filter中等号使用“==”  [<2,jack,jack1234>]
# res = Session.query(User).filter(User.id > 1).filter(User.id < 3).all() #多个查询条件[<2,jack,jack1234>]
# print(res) #[<1,alex,alex1234>] 通过__repr__函数来实现
# # print(res[0].name,res[0].passwd)#alex alex1234
#
# #修改
# res = Session.query(User).filter(User.id > 1).filter(User.id < 3).first() #[<2,jack,jack1234>]
# res.name = "Jack"
# res.passwd = "jack123456"
# Session.commit()
#
#
#
# # Session.rollback() #回滚
# print(".............")
# print(Session.query(User).all()) #获取所有数据 [<1,alex,alex1234>, <2,Jack,jack123456>]
# print(Session.query(User.name).all()) #获取所有的name[('alex',), ('Jack',)]
# print(Session.query(User).filter(User.name.like("Ja%")).count()) #查询结果计数 1
# from sqlalchemy import func
# print(Session.query(func.count(User.name),User.name).group_by(User.name).all())  #groupby 分组[(1, 'alex'), (1, 'Jack')]
# print(Session.query(User).filter(User.name.in_(["Jack","alex"])).all()) #[<1,alex,alex1234>, <2,Jack,jack123456>]
# for name in ["jarry","harry","polly","hery","candly"]:
#     Session.add(Student(name=name,register_date="2018-07-31",gender=random.choice(["F","M"])))
# Session.commit()

#连表查询

#两个表之间外键关联




