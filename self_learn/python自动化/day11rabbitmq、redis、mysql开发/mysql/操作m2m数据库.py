#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/8/1 16:11
from sqlalchemy.orm import sessionmaker
import orm_m2m
Session_class = sessionmaker(bind=orm_m2m.engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class() #生成session实例

b1 = orm_m2m.Book(name="跟Alex学Python") #新增书籍数据
b2 = orm_m2m.Book(name="跟Alex学把妹")
b3 = orm_m2m.Book(name="跟Alex学装逼")
b4 = orm_m2m.Book(name="跟Alex学开车")

a1 = orm_m2m.Author(name="Alex")#新增作者数据
a2 = orm_m2m.Author(name="Jack")
a3 = orm_m2m.Author(name="Rain")
b1.authors = [a1,a2]  #创建数据与组着的对应关系
b2.authors = [a1,a2,a3]
# session.add_all([b1,b2,b3,b4,a1,a2,a3]) #添加数据
# session.commit()
print('--------通过书表查关联的作者---------')
book_obj = session.query(orm_m2m.Book).filter(orm_m2m.Book.name=="跟Alex学Python").first()
print(book_obj.name,book_obj.authors)  #跟Alex学Python [Alex, Jack]
print('--------通过作者表查关联的书---------')
auth_obj = session.query(orm_m2m.Author).filter(orm_m2m.Author.name=="Alex").first()
print(auth_obj.name,auth_obj.books) #Alex [跟Alex学Python, 跟Alex学把妹]

print('--------直接删除作者---------')
author_obj =session.query(orm_m2m.Author).filter(orm_m2m.Author.name=="Alex").first()
session.delete(auth_obj)
session.commit() #删除了authors表中alex的信息已经关联表中与alex对应的书籍信息

print('--------通过书名删除作者---------')
author_obj =session.query(orm_m2m.Author).filter(orm_m2m.Author.name=="Alex").first()
book_obj = session.query(orm_m2m.Book).filter(orm_m2m.Book.name=="跟Alex学把妹").first()
book_obj.authors.remove(author_obj)
session.commit() ##从关联表里删除了本书里删除一个作者