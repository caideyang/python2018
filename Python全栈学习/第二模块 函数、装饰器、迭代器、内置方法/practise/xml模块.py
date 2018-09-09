#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/9 5:47

import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')  #解析test.xml文件，生成parse对象
root = tree.getroot()  #获取根节点
# print(root.tag)  #获取根节点的tag名
#
# #遍历xml文档
# for child in root:
#     print("---",child.tag,child.attrib)  #tag 标签名；attrib 标签里的属性键值对
#     for i in child:
#         print("--------",i.tag,i.attrib,i.text)  # test 标签对应的文本
#
# # 只遍历year节点
# for node in root.iter('year'):
#     print(node.tag,node.text)

# #修改
# for node in root.iter('year'):
#     new_year = int(node.text) + 1  #将year标签里所有的文本值加1
#     node.text = str(new_year)   #将新值赋给该文本
#     node.set("attr_test","no")   #设置year标签里的attr_test属性值为no
#
# tree.write('output.xml')  #将数据写入新的文件output.xml

# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
# tree.write('output.xml')
for country in root.findall('country'):
    if int(country.iter('rank').text) >2 :
        country.iter('population').text =  '100000'
tree.write('output.xml')


if __name__ == "__main__":
    pass