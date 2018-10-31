#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/31 15:11
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine(
"mysql+pymysql://cdy:passwd@192.168.56.11/test",
 encoding='utf-8', echo=True
)
Base = declarative_base() #s生成orm基类
class User(Base):
    __tablename__ = "user" #数据库表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    passwd = Column(String(64))


Base.metadata.create_all(engine) #创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

user_obj1 = User(name="alex", passwd="alex3714")  # 生成你要创建的数据对象
user_obj2 = User(name="jack", passwd="jack3714")  # 生成你要创建的数据对象
print(user_obj1.name, user_obj1.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
Session.add(user_obj1)  # 把要创建的数据对象添加到这个session里， 一会统一创建
Session.add(user_obj2)  # 把要创建的数据对象添加到这个session里， 一会统一创建
print(user_obj1.name, user_obj1.id)  # 此时也依然还没创建

Session.commit()  # 现此才统一提交，创建数据

#
# if __name__ == "__main__":
#     pass