#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/8/2 15:38


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Table,DATE,ForeignKey,Enum,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
bindhost_m2m_userprofile = Table(   #主机表与堡垒机登录用户表多对多的对应关系
    'bindhost_m2m_userprofile',Base.metadata,
    Column("bindhost_id",Integer,ForeignKey("bind_host.id")),
    Column("userprofile_id",Integer,ForeignKey("user_profile.id"))
)
bindhost_m2m_hostgroup = Table(   #主机表与主机组表多对多的对应关系
    'bindhost_m2m_hostgroup',Base.metadata,
    Column("bindhost_id",Integer,ForeignKey("bind_host.id")),
    Column("hostgroup_id",Integer,ForeignKey("host_group.id"))
)
hostgroup_m2m_userprofile = Table(   #主机组表与堡垒机登录用户表多对多的对应关系
    'hostgroup_m2m_userprofile',Base.metadata,
    Column("userprofile_id",Integer,ForeignKey("user_profile.id")),
    Column("hostgroup_id",Integer,ForeignKey("host_group.id"))
)

class Host(Base):
    __tablename__ = "hosts" #主机表
    id = Column(Integer,primary_key=True)
    ip = Column(String(64),nullable=False)
    name = Column(String(63),nullable=False)
    port = Column(Integer,default=22)

    # remote_users = relationship("RemoteUser",secondary=host_m2m_remoteuser,backref="hosts")  #主机表与远程用户的关联关系

    def __repr__(self):
        return self.name
class HostGroup(Base):
    __tablename__ = "host_group" #主机组表
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    bind_hosts = relationship("BindHost",secondary="bindhost_m2m_hostgroup",backref="host_groups")

    def __repr__(self):
        return self.name

class RemoteUser(Base):
    __tablename__ = "remote_user" #远程主机登录用户表
    __table_args__ = (UniqueConstraint('auth_type', 'name', 'password', name='_user_passwd_uc'),)
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    password = Column(String(128),nullable=True)
    # auth_type = Column(Enum("ssh-password","ssh-key"),nullable=False)
    AuthTypes = [
        ('ssh-password', 'SSH/Password'),
        ('ssh-key', 'SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes))



    def __repr__(self):
        return self.name

class BindHost(Base):
    """
    主机、远程主机用户/密码  关联关系
    192.168.16.11 root  bj_group
    """
    __tablename__ = "bind_host"
    __table_args_ = (UniqueConstraint("host_id","remoteuser_id",name="bindhost_and_user_uc"))  #联合唯一
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer,ForeignKey("hosts.id"))
    remoteuser_id = Column(Integer,ForeignKey("remote_user.id"))
    # hostgroup_id = Column(Integer,ForeignKey("host_group.id"))

    host = relationship("Host",backref="bindhosts")
    remoteuser = relationship("RemoteUser",backref="bindhosts")
    # hostgroup = relationship("HostGroup",backref="bindhosts")

    def __repr__(self):
        return "<%s--%s--%s>" %(self.host.ip,
                                self.remoteuser.name
                                # self.hostgroup.name
        )



class UserProfile(Base):
    __tablename__ = "user_profile"  #堡垒机用户账号表
    id = Column(Integer, primary_key=True)
    name = Column(Integer,nullable=False)
    passwd = Column(String(128),nullable=False)
    bind_hosts = relationship("BindHost",secondary="bindhost_m2m_userprofile",backref="user_profiles")
    host_groups = relationship("HostGroup", secondary="hostgroup_m2m_userprofile", backref="user_profiles")
    def __repr__(self):
        return self.name

# class Auditlog(Base):
#     __tablename__ = "audit_log"  #审计日志表
#     id = Column(Integer, primary_key=True)
#     date = Column(DATE,nullable=False)
#     u_id = Column(Integer,ForeignKey("user_profile.id"))
#     host_id = Column(Integer,ForeignKey("hosts.id"))
#     cmd = Column(String(1024),nullable=False)
#
#     def __repr__(self):
#         pass


if __name__ == "__main__":
    engine = create_engine(
        "mysql+pymysql://cdy:passwd@192.168.56.11/baoleiji?charset=utf8",  # 数据库连接
        encoding="utf-8",  # 编码格式
        echo=True  # 运行输出日志,True输出，False不输出
    )
    Base.metadata.create_all(engine) #创建所有表结构