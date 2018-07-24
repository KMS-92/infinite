# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 22:46:27 2018

@author: 虞姬1987
"""
#（全球五天天气）练习题4
#1.打印出每天18:00的天气信息，温度，情况，气压，最高温度，最低温度
#2.写出英文版的天气-天气情况，用户输入英文  application应用
#3.打印温度折线表 
#               1----------------
#               2-----------------------
#               3------------
#               4------------------
#4.获取所有温度，并且排序   (sorted([1,4,-1,8])########使用此方法排序)
#5.友情提示：根据温度选择穿衣，打伞，出门   (可选)


#################################第一个问题####################################
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r  #导入联网工具包，名为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json  #将字符串转换成字典
data=json.loads(data)

#data字典-》list列表-》？ index字典-》dt_txt变量
#data字典-》list列表-》？ index字典-》main字典-》temp变量
#data字典-》list列表-》？ index字典-》weather列表-》0 index字典-》description变量
#data字典-》list列表-》？ index字典-》main字典-》pressure变量
#data字典-》list列表-》？ index字典-》main字典-》temp_max变量
#data字典-》list列表-》？ index字典-》main字典-》temp_min变量
print(str(data['list'][2]['dt_txt'])+'的天气信息')
print('温度:'+str(data['list'][2]['main']['temp']))
print('情况:'+str(data['list'][2]['weather'][0]['description']))
print('气压:'+str(data['list'][2]['main']['pressure']))
print('最高温度:'+str(data['list'][2]['main']['temp_max']))
print('最低温度:'+str(data['list'][2]['main']['temp_min']))
print(str(data['list'][10]['dt_txt'])+'的天气信息')
print('温度:'+str(data['list'][10]['main']['temp']))
print('情况:'+str(data['list'][10]['weather'][0]['description']))
print('气压:'+str(data['list'][10]['main']['pressure']))
print('最高温度:'+str(data['list'][10]['main']['temp_max']))
print('最低温度:'+str(data['list'][10]['main']['temp_min']))
print(str(data['list'][18]['dt_txt'])+'的天气信息')
print('温度:'+str(data['list'][18]['main']['temp']))
print('情况:'+str(data['list'][18]['weather'][0]['description']))
print('气压:'+str(data['list'][18]['main']['pressure']))
print('最高温度:'+str(data['list'][18]['main']['temp_max']))
print('最低温度:'+str(data['list'][18]['main']['temp_min']))
print(str(data['list'][26]['dt_txt'])+'的天气信息')
print('温度:'+str(data['list'][26]['main']['temp']))
print('情况:'+str(data['list'][26]['weather'][0]['description']))
print('气压:'+str(data['list'][26]['main']['pressure']))
print('最高温度:'+str(data['list'][26]['main']['temp_max']))
print('最低温度:'+str(data['list'][26]['main']['temp_min']))
print(str(data['list'][34]['dt_txt'])+'的天气信息')
print('温度:'+str(data['list'][34]['main']['temp']))
print('情况:'+str(data['list'][34]['weather'][0]['description']))
print('气压:'+str(data['list'][34]['main']['pressure']))
print('最高温度:'+str(data['list'][34]['main']['temp_max']))
print('最低温度:'+str(data['list'][34]['main']['temp_min']))


#################################第二个问题####################################
#data字典-》list列表-》？ index字典-》weather列表-》0 index字典-》main变量
city=input('please input city to search:')
url='http://api.openweathermap.org/data/2.5/forecast?q='+city+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r  #导入联网工具包，名为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json  #将字符串转换成字典
data=json.loads(data)

print(data['list'][2]['dt_txt'])
print('temp is:'+str(data['list'][2]['main']['temp']))
print('description is:'+str(data['list'][2]['weather'][0]['main']))
print('pressure is:'+str(data['list'][2]['main']['pressure']))
print('temp_max is:'+str(data['list'][2]['main']['temp_max']))
print('temp_min is:'+str(data['list'][2]['main']['temp_min']))
print(data['list'][10]['dt_txt'])
print('temp is:'+str(data['list'][10]['main']['temp']))
print('description is:'+str(data['list'][10]['weather'][0]['main']))
print('pressure is:'+str(data['list'][10]['main']['pressure']))
print('temp_max is:'+str(data['list'][10]['main']['temp_max']))
print('temp_min is:'+str(data['list'][10]['main']['temp_min']))
print(data['list'][18]['dt_txt'])
print('temp is:'+str(data['list'][18]['main']['temp']))
print('description is:'+str(data['list'][18]['weather'][0]['main']))
print('pressure is:'+str(data['list'][18]['main']['pressure']))
print('temp_max is:'+str(data['list'][18]['main']['temp_max']))
print('temp_min is:'+str(data['list'][18]['main']['temp_min']))
print(data['list'][26]['dt_txt'])
print('temp is:'+str(data['list'][26]['main']['temp']))
print('description is:'+str(data['list'][26]['weather'][0]['main']))
print('pressure is:'+str(data['list'][26]['main']['pressure']))
print('temp_max is:'+str(data['list'][26]['main']['temp_max']))
print('temp_min is:'+str(data['list'][26]['main']['temp_min']))
print(data['list'][34]['dt_txt'])
print('temp is:'+str(data['list'][34]['main']['temp']))
print('description is:'+str(data['list'][34]['weather'][0]['main']))
print('pressure is:'+str(data['list'][34]['main']['pressure']))
print('temp_max is:'+str(data['list'][34]['main']['temp_max']))
print('temp_min is:'+str(data['list'][34]['main']['temp_min']))



################################第三四个问题####################################
print('温度折线图为：')
print('第一天:'+'-'*int(data['list'][2]['main']['temp']))
print('第二天:'+'-'*int(data['list'][10]['main']['temp']))
print('第三天:'+'-'*int(data['list'][18]['main']['temp']))
print('第四天:'+'-'*int(data['list'][26]['main']['temp']))
print('第五天:'+'-'*int(data['list'][34]['main']['temp']))

all_temp=[data['list'][2]['main']['temp'],
         data['list'][10]['main']['temp'],
         data['list'][18]['main']['temp'],
         data['list'][26]['main']['temp'],
         data['list'][34]['main']['temp']]
print('温度排序为：')
print(sorted([all_temp]))
