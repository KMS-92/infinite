# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:57:25 2018

@author: 虞姬1987
"""
#（淘宝客户端）练习题6:
#禁止使用for while 
#1.显示4个商品并打印分割线，只要第一个36个商品信息
#2.列出36个商品
#3.获取所有的商品价格并且给商品排序，从高到低排序
#4.按照销量排序
#5.商品过滤，只要15天退款或者包邮的商品信息，显示

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
    for i in range(0,36):
        print('第'+str(i+1)+'个商品的信息为：')
        print('商品名称：'+str(data['mods']['itemlist']['data']['auctions'][i]['title']))
        print('商品售价：'+str(data['mods']['itemlist']['data']['auctions'][i]['view_price']))
        print('商品邮费：'+str(data['mods']['itemlist']['data']['auctions'][i]['view_fee']))
        print('商品销量：'+str(data['mods']['itemlist']['data']['auctions'][i]['view_sales']))
        if (i+1)%4==0:
            print('-'*50)
show()
 
ls=[]      
def price():
    for i in range(0,36):
        ####float型
        m=float(data['mods']['itemlist']['data']['auctions'][i]['view_price'])
        ls.append(m)
    return ls
price()
a=sorted(ls)
b=list(reversed(a))
print('按照商品价格从高到低的排序为：')
print(b)

lls=[]
def sales():
    for i in range(0,36):
        m=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        n=int(m[0:-3])################################
        lls.append(n)
    return lls
sales()
c=sorted(lls)
d=list(reversed(c))
print('按照商品销量从高到低的排序为：')
print(d)

def fee():
    for i in range(0,36):
        m=float(data['mods']['itemlist']['data']['auctions'][i]['view_fee'])
        if m==0:
            print('第'+str(i+1)+'件商品包邮')
fee()
        
###########################按照要求不使用循环做的###############################

    