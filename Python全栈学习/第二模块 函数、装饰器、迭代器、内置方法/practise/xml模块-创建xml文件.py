#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/9 6:24

import xml.etree.ElementTree as ET

root = ET.Element("namelist") #根节点
name = ET.SubElement(root, "name", attrib={"enrolled": "yes"}) #添加root的子节点，设置节点属性
n = ET.SubElement(name,'name') #添加name节点的子节点name
n.text = "CWQ"  #给节点的文本赋值
age = ET.SubElement(name, 'age', attrib={"checked": "no"})
age.text = "31"
sex = ET.SubElement(name,"sex")
sex.text = 'F'

et = ET.ElementTree(root ) #生成文档对象
et.write("build_out.xml", encoding="utf-8",xml_declaration=True)  #写入文本
