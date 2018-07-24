# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 22:19:50 2018

@author: 虞姬1987
"""
#（天气预报）练习题3：
#1.通过复制联网天气代码，获取老家天气字典
#2.打印温度temp,天气情况descprition,天气气压pressure

url='http://api.openweathermap.org/data/2.5/weather?q=shanghai&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
import urllib.request as r #导入联网工具包，名为r， 打开网址，读取内容转换为str
data=r.urlopen(url).read().decode('utf-8','ignore')

import json #字符串转字典的工具包
data=json.loads(data)

#data字典-》main字典-》temp变量
print(data['main']['temp'])
#data字典-》weather字典-》description变量
print(data['weather'][0]['description'])
#data字典-》main字典-》pressure变量
print(data['main']['pressure'])