#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/8/1 11:28

from sqlalchemy import create_engine,engine
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker

engine = create_engine(
    "mysql+pymysql://cdy:passwd@192.168.56.11/oldboydb?charset=utf8", #数据库连接
    encoding="utf-8", #编码格式
    echo=False  #运行输出日志,True输出，False不输出
)
Base = declarative_base()

class Address(Base): #地址表
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(200))
    city = Column(String(64))
    state = Column(String(64))


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    cus_id = Column(Integer, ForeignKey("address.id"))
    mail_id = Column(Integer, ForeignKey("address.id"))


Base.metadata.create_all(engine) #创建表结构,如果不存在则创建，存在则不创建

#插入
Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class
Session = Session_class()
# addr1 = Address(street="天通苑",city="昌平",state="北京")
# addr2 = Address(street="高教园",city="昌平",state="北京")
# addr3 = Address(street="燕郊",city="廊坊",state="河北")
# Session.add_all([addr1,addr2,addr3])
custom1 = Customer(name="Alex",cus_id=1,mail_id=2)
Session.add(custom1)
Session.commit()