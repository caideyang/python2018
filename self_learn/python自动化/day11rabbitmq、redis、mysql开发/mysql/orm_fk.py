#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/8/1 10:39
from sqlalchemy import create_engine,engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Enum,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine(
    "mysql+pymysql://cdy:passwd@192.168.56.11/oldboydb?charset=utf8", #数据库连接
    encoding="utf-8", #编码格式
    echo=False  #运行输出日志,True输出，False不输出
)
Base = declarative_base() #生成orm基类

class Student(Base):
    __tablename__ = "student"  # 学生表
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "<name:%s,register_date:%s>" %(self.name,self.register_date)

class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer,primary_key=True)
    day = Column(Integer)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey("student.id"))
    student = relationship("Student",backref="my_study_record") #将关联关系反射到study_record表,允许你在student表中通过backref字段反向查询所有他在study_reocord表中的记录
    def __repr__(self):
        return "<name:%s,day:%s,status:%s>" %(self.student.name,self.day,self.status)

Base.metadata.create_all(engine) #创建表结构,如果不存在则创建，存在则不创建
Session_class = sessionmaker(bind=engine) #创建与数据库的会话session 类
session = Session_class() #实例化这个seesion类
#查找
res = session.query(StudyRecord).filter(StudyRecord.stu_id == 1).all()
print(res) #[<name:Alex,day:1,status:YES>, <name:Alex,day:2,status:YES>, <name:Alex,day:3,status:YES>]
res = session.query(Student).first()
print(res) #<name:Alex,register_date:2014-05-21>
for i in res.my_study_record:
    print(i) #<name:Alex,day:1,status:YES <name:Alex,day:2,status:YES> <name:Alex,day:3,status:YES>
