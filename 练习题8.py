# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:27:30 2018

Url=url'&s='+str(44*i)
保存为csv格式的方法 ：
在Python中打开hainan.txt-->File-->save as-->(在输入名称中输入)-->hainan.csv

@author: 虞姬1987
"""
#（淘宝数据获取）练习题8：裙子 海南
#获取URL数据，直接保存到文件中，保存100个URL的数据每一个URL数据为记事本中的1行，
#总100行。每个人城市不相同并保存为csv格式

#网址后加&ajax=true
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E6%B5%B7%E5%8D%97&bcoffset=4&p4ppushleft=1%2C48&ajax=true'
import urllib.request as r#导入联网工具包，名为r

def Req():
    for i in range(100):
        Url=url+'&s='+str(i*44)
        try:
            f=r.urlopen(Url)#HTTP正常状态码 200
            if f.getcode()==200:
                data=f.read().decode('utf-8','ignore')
        except Exception as err:
            print('网络请求错误，正在重试中...')
            i=i-1
            break
        try:
            fileURL=open('hainan.txt','a+',encoding='utf-8')
            fileURL.write(data+'\n')
            fileURL.close()
        except Exception as err:
            print('文件写入错误，正在重试中...')
            break
        print('第'+str(i+1)+'页数据爬取成功')
Req()
