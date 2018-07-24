# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 19:22:04 2018

@author: 虞姬1987
"""
#（循环语句）练习题7：
#1.使用多选其一完成天气的提醒，淘宝客户端
#2.一定要多次使用for循环，偶尔使用while在淘宝客户端中
#3.使用到break或者continue在淘宝客户端中

url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r  #导入联网工具包，名为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json  #将字符串转换成字典
data=json.loads(data)

#data字典-》list列表-》？ index字典-》main字典-》temp变量
#data字典-》list列表-》？ index字典-》weather列表-》0 index字典-》main变量
print('温馨提示：')
def day(a,b): 
    print('day'+str(a)+'的天气情况：')
    print('温度:'+str(data['list'][b]['main']['temp'])+' '+'情况:'+str(data['list'][2+b*8]['weather'][0]['main']))
    temp=data['list'][b]['main']['temp']
    main=data['list'][2+b*8]['weather'][0]['main']
    if temp>=30:
        print('温度较高，建议身着短裤半袖、裙子，如需出门请携带遮阳伞，避免晒伤。')
    elif temp>=20 and main=='Rain':
        print('温度适宜，有降雨，建议身着长裤短袖，如需出门请携带雨伞，以防淋雨感冒。')
    elif temp>=20:
        print('温度适宜，无降雨，建议身着长裤短袖，宜出门郊游野炊，宜运动。')
    elif main=='Rain':
        print('气温较低，且有降雨，建议身着长裤外套，不宜出门。')
    else:
        print('气温相对较低，无降雨，建议身着长袖外套，注意保暖，宜出门，宜运动')
day(1,0)
day(2,1)
day(3,2)
day(4,3)
day(5,4)

url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

#data字典-》mods字典-》itemlist字典-》data字典-》auctions列表-》0 index字典-》title变量
#data字典-》mods字典-》itemlist字典-》data字典-》auctions列表-》0 index字典-》view_price变量
#data字典-》mods字典-》itemlist字典-》data字典-》auctions列表-》0 index字典-》view_fee变量
#data字典-》mods字典-》itemlist字典-》data字典-》auctions列表-》0 index字典-》view_sales变量
def show():
    for i in range(36):
        print('第'+str(i+1)+'个商品的信息为：')
        print('商品名称：'+str(data['mods']['itemlist']['data']['auctions'][i]['title']))
        print('商品售价：'+str(data['mods']['itemlist']['data']['auctions'][i]['view_price']))
        print('商品邮费：'+str(data['mods']['itemlist']['data']['auctions'][i]['view_fee']))
        print('商品销量：'+str(data['mods']['itemlist']['data']['auctions'][i]['view_sales']))
        
        price=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
        fee=float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])
        if fee>0 and price>=400:
            print('此商品不包邮,价格较高')
        elif fee>0 and price>=200:
            print('此商品不包邮,价格适宜')
        elif fee>0:
            print('此商品不包邮,价格优惠')
        elif fee==0 and price>=400:
            print('此商品包邮,价格较高')
        elif fee==0 and price>=200:
            print('此商品包邮,价格适宜')
        else:
            print('此商品包邮,价格优惠')
        print(' ')
         
        if (i+1)%4>0:
            continue
        else:
            print('-'*50)
            
        while i>=35:
            print('前36个商品信息已输出完毕')
            break
show()
        
        
    
    
