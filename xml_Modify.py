# _*_ coding: utf-8 _*_
#   Time:     2022/04/30 21.25
#   Author:   Ricky Fang
#   Version:  V1
#   File:     xml_Modify.py
#   Describe: 批量修改.xml文件，用于网络训练


import os
import os.path
from xml.etree.ElementTree import parse, Element



# .xml文件的绝对地址
path = "/home/ricky/下载/faster-rcnn-pytorch-master/VOCdevkit/VOC2007/Annotations/"



# 得到该文件夹下的所有.xml文件
files = os.listdir(path)  
s = []



# 遍历Annotations文件夹
print('============智能运载装备研究所============')
for xmlFile in files:
    # 判断是否是文件夹
    if not os.path.isdir(xmlFile):
        print(xmlFile)
        pass
    newStr = os.path.join(path, xmlFile)
    dom = parse(newStr)
    root = dom.getroot()
    #获得文件名(分离文件名和扩展名)
    part = os.path.splitext(xmlFile)[0]
    # 文件名+后缀
    part1 = part + '.jpg'
    # path里的新属性值：
    newStr1 = '/home/ricky/下载/faster-rcnn-pytorch-master/VOCdevkit/VOC2007/JPEGImages/' + part1
    newStr2 = 'VOC2007'
    
    
    
    #  root.find('你要改的属性').text = 句柄 
    
    root.find('path').text = newStr1  
    root.find('filename').text = part1
    root.find('folder').text = newStr2
    
    #  root.find('你要改的属性').text = 句柄 
    
    
    
    print('============智能运载装备研究所============')
    dom.write(newStr, xml_declaration=True)
    pass

