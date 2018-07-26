# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:06:19 2018

@author: 虞姬1987
"""

import json
fileLists=open('面膜在大连.txt',encoding='utf-8')
data=json.loads(fileLists.readline())
pricePeople={
        '0-50':0,
        '50-100':0,
        '100-200':0,
        '200-500':0,
        '500-1000':0,
        '大于1000':0
        }
for i in data:
    a=float(i["view_price"])
    if a>=0 and a<50:
        pricePeople['0-50']=pricePeople['0-50']+int(i["view_sales"][:-3])
    elif a>=50 and a<100:
        pricePeople['50-100']=pricePeople['50-100']+int(i["view_sales"][:-3])
    elif a>=100 and a<200:
        pricePeople['100-200']=pricePeople['100-200']+int(i["view_sales"][:-3])
    elif a>=200 and a<500:
        pricePeople['200-500']=pricePeople['200-500']+int(i["view_sales"][:-3])
    elif a>=500 and a<1000:
        pricePeople['500-1000']=pricePeople['500-1000']+int(i["view_sales"][:-3])
    else:
        pricePeople['大于1000']=pricePeople['大于1000']+int(i["view_sales"][:-3])
print(pricePeople)