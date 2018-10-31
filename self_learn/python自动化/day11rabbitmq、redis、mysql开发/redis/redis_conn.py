#!/usr/bin/python3
#encoding:utf-8
#@Author:CaiDeyang
#@Time: 2018/7/30 5:51

import redis
pool = redis.ConnectionPool(host="192.168.56.11",port=6379) #创建一个连接池，这样不用每次请求redis数据时都去连接一次redis，降低系统开销
conn = redis.Redis(connection_pool=pool)
# conn = redis.Redis(host="192.168.56.11",port=6379) #建立一个连接

# conn.set("name","caideyang")
# print(conn.get('name')) #b'caideyang'
# conn.set("age1",32,ex=20,xx=True)
# conn.mset(name="cwq",age=30,salary=100000)
# conn.mset({"name":"caideyang","age":31,"salary":20000})
# print(conn.mget("name","age","salary")) #[b'caideyang', b'31', b'20000']
# print(conn.get("age1")) #None,已经过期
# print(conn.getset("name","chengwanqing")) #b'caideyang' 获取name之前的值，并将其改为chengwanqing
# print(conn.get("name")) #获取name的新值b'chengwanqing'
# print(conn.getrange("name",1,2)) #b'he'
# conn.setrange("name",1,"H")#修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
# print(conn.get("name")) #b'cHengwanqing'
#
# conn.set("content","Hello,Caideyang!")
# conn.setbit("content",7,1)
# print(conn.get("content")) #b'Iello,Caideyang!'
#
# conn.set("name","蔡德阳")
# for i in conn.get("name"):
#     #对于utf-8，每一个汉字占 3 个字节，那么 "蔡德阳" 则有 9个字节, 对于汉字，for循环时候会按照 字节 迭代，那么在迭代时，将每一个字节转换 十进制数，然后再将十进制数转换成二进制
#     print(bin(i)) #0b11101000 0b10010100 0b10100001 0b11100101 0b10111110 0b10110111 0b11101001 0b10011000 0b10110011
# conn.setbit("name",7,1)
# print(conn.get("name").decode()) #锡德阳
# conn.hset("info",'name','caideyang')
# conn.hset("info","age",32)
# print(conn.hget("info","name")) #b'caideyang'
#
# print(conn.hmget("info","name","age")) #[b'caideyang', b'32']
# print(conn.hgetall("info"))#{b'name': b'caideyang', b'age': b'32'}
# print(conn.hkeys("info"))#[b'name', b'age']
# print(conn.hvals("info"))# [b'caideyang', b'32']
# conn.hmset("info",{"salary":30000,"addr":"Chaoyang district JiangtaiRoad"})
# print(conn.hgetall("info"))#{b'name': b'caideyang', b'age': b'32', b'salary': b'30000', b'addr': b'Chaoyang district JiangtaiRoad'}
# print(conn.hlen("info")) # 4
# print(conn.hexists("info","name")) #True
# conn.hdel("info","salary")
# print(conn.hgetall("info"))#{b'name': b'caideyang', b'age': b'32', b'addr': b'Chaoyang district JiangtaiRoad'}
# print(conn.hexists("info","salary")) #False
# conn.hincrby("info","age",1)
# print(conn.hget("info","age")) #b'33'
# print(conn.hkeys("info"))#[b'name', b'age', b'addr']
# print(conn.hscan("info",0,"a*"))#(0, {b'age': b'33', b'addr': b'Chaoyang district JiangtaiRoad'})
# print(conn.hscan("info",0,"*me")) #(0, {b'name': b'caideyang'})
# print(conn.hscan("info",0,"a*r"))#(0, {b'addr': b'Chaoyang district JiangtaiRoad'})
# conn.delete("List1")
# conn.delete("List2")
# conn.lpush("List1","caideyang") #从左侧插入，rpush从右侧插入
# conn.lpush("List1","chengwanqing")
# conn.lpush("List1","caijincheng")
# conn.lpush("List1","zhoujun")
# conn.rpush("List1","zhutongfeng") #从右侧插入
# conn.lpushx("List2","caixiangyou") #lpushx 当List1存在时才插入成功
# print(conn.llen("List1"))
# print(conn.lrange("List1",0,-1)) #[b'zhoujun', b'caijincheng', b'chengwanqing', b'caideyang', b'zhutongfeng']
# conn.lset("List1",1,"Chengwanqing") #将List1列表中索引为1的值改成Chengwanqing
# conn.linsert("List1","AFTER","caideyang","deyangcai") #在值“caideyang”之后插入“deyangcai”
# print(conn.lrange("List1",0,-1)) #[b'zhoujun', b'Chengwanqing', b'chengwanqing', b'caideyang', b'deyangcai', b'zhutongfeng']
# conn.lrem("List1","deyangcai",1) #删除列表中值为deyangcai的1条数据，如果最后一个参数为0，则删除所有值为“deyangcai”的数据
# print(conn.lpop("List1")) #b'zhoujun',类似于Python的列表中的pop函数，从左侧弹出一个数据，rpop()从右侧弹出一个数据
# print(conn.lindex("List1",2)) #b'caideyang' 获取索引为2的值
# conn.ltrim("List1",1,3) #在List1列表中移除没有在1-3索引之间的值
# conn.lpush("List2","cdy1")
# conn.lpush("List2","cdy2")
# conn.lpush("List2","cdy3")
# conn.lpush("List2","cdy4")
# print(conn.lrange("List2",0,-1)) #[b'cdy4', b'cdy3', b'cdy2', b'cdy1']
# conn.rpoplpush("List2","List1") #将List2列表中最右侧的值pop出来插入到List1列表的最左侧
# conn.brpoplpush("List2","List1",30) #将List2列表中最右侧的值pop出来插入到List1列表的最左侧,当List2中没有值时，阻塞等待30秒，0表示永远阻塞
# print(conn.lrange("List1",0,-1))#[b'cdy2', b'cdy1', b'chengwanqing', b'caideyang', b'zhutongfeng']
# print(conn.lrange("List2",0,-1))#[b'cdy4', b'cdy3']

conn.sadd("Set1","a")
conn.sadd("Set1","b")
conn.sadd("Set1","c")
conn.sadd("Set1","d")
conn.sadd("Set1","e")
conn.sadd("Set1","f")
conn.sadd("Set2","b")
conn.sadd("Set2","c")
conn.sadd("Set2","d")
print(conn.scard("Set1")) #3, Set1中集合中元素的个数
print(conn.sdiff("Set1","Set2")) #比对在第一个集合中存在，但在其他集合中不存在的
conn.sdiffstore("Set3","Set1","Set2") #比对在Set1集合中存在，但在其他集合Set2中不存在的,比对结果存入Set3
conn.sinter("Set4","Set1","Set2") #求并集
print(conn.sdiff("Set4"))



