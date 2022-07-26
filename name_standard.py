# _*_ coding: utf-8 _*_
#   Time:     2022/04/30 21.25
#   Author:   Ricky Fang
#   Version:  V1
#   File:     name_standard.py
#   Describe: 批量修改.xml和jpg文件的名字，用于规范VOC数据集


import os
# .xml文件的绝对路路径
path = "//home//ricky//下载//faster-rcnn-pytorch-master//VOCdevkit//VOC2007//Annotations"
# .jpg文件的绝对路路径
# path = "//home//ricky//下载//faster-rcnn-pytorch-master//VOCdevkit//VOC2007//JPEGImages"
filelist = os.listdir(path) 
count=0
for file in filelist:
    print(file)
for file in filelist:   
    Olddir=os.path.join(path,file)  
    if os.path.isdir(Olddir):  
        continue
    filename=os.path.splitext(file)[0]  
    filetype=os.path.splitext(file)[1]   
    Newdir=os.path.join(path,str(count).zfill(6)+filetype)  
    os.rename(Olddir,Newdir)
    count+=1
