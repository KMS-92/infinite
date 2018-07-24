# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:04:40 2018

@author: Administrator
"""
#（可视化展示）练习11:
#1.获取学校名
#2.获取学校招生人数
#3.在Echarts展示

f=open('E:\\大数据实训\\课程作业\\切片母本.txt',encoding='gbk').readlines()
schoolls=[]
data=[]
for line in f:
    schoolls.append(line.split('(')[1].split(',')[0])
    data.append(line.split(',')[1].split(')')[0])
    print(schoolls)
    print(data)
    