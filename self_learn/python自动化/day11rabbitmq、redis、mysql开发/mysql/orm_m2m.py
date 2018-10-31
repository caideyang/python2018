#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/8/1 15:51

from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://cdy:passwd@192.168.56.11/oldboydb?charset=utf8", #数据库连接
    encoding="utf-8", #编码格式
    echo=False  #运行输出日志,True输出，False不输出
)

Base = declarative_base() #创建一个基类
book_m2m_author = Table(
    'book_m2m_author',Base.metadata,
    Column("book_id",Integer,ForeignKey("books.id")),
    Column("author_id",Integer,ForeignKey("authors.id"))
)
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_data = Column(DATE)
    authors = relationship("Author",secondary=book_m2m_author,backref="books")

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer,primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

Base.metadata.create_all(engine) #创建表结构



