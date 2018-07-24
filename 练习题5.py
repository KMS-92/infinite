# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:58:56 2018

@author: 虞姬1987
"""
#（函数）练习题5：
#1.练习4使用到函数 使用到list的一些功能
#2.优化代码 用函数的方式修改练习4 输出每一天的天气（函数）
#3.打印温度折线图，使用函数来优化（必须要有返回值）

url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r #导入联网工具包，名为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json #将字符串转换为字典
data=json.loads(data)

#weather列表
#data字典-》list列表-》？ index字典-》dt_txt变量
#data字典-》list列表-》？ index字典-》main字典-》temp变量
#data字典-》list列表-》？ index字典-》weather列表-》0 index字典-》description变量
#data字典-》list列表-》？ index字典-》main字典-》pressure变量
#data字典-》list列表-》？ index字典-》main字典-》temp_max变量
#data字典-》list列表-》？ index字典-》main字典-》temp_min变量
def day(a,b): 
    print('day'+str(a)+'的天气情况：')
    print('温度:'+str(data['list'][b]['main']['temp']))
    print('情况:'+str(data['list'][b]['weather'][0]['description']))
    print('气压:'+str(data['list'][b]['main']['pressure']))
    print('最高温度:'+str(data['list'][b]['main']['temp_max']))
    print('最低温度:'+str(data['list'][b]['main']['temp_min'])) 
day(1,2)
day(2,10)
day(3,18)
day(4,26)
day(5,34)

def LSC(n):
    return data['list'][2+n*8]['main']['temp']
a=LSC(0)
b=LSC(1)
c=LSC(2)
d=LSC(3)
e=LSC(4)
m=[a,b,c,d,e]
print('温度排序为：')
print(sorted(m))

#data字典-》list列表-》？ index字典-》weather列表-》0 index字典-》main变量
def weather(a,b):
    print('day'+str(a))
    print(data['list'][b]['weather'][0]['main'])
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)

def TempLine(a,x):
    line='day'+str(a)+'-'*int(data['list'][2+x*8]['main']['temp'])
    return line
print('Temperature line diagram:') #plot
print(TempLine(1,0))
print(TempLine(2,1))
print(TempLine(3,2))
print(TempLine(4,3))
print(TempLine(5,4))

