# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:26:55 2018

@author: 君
"""

import json
import urllib.request as r
import time
#这里是关键词，修改就好
keyword = '面膜'
#这里是地点城市，修改即可
place = '南宁'
#下面是转码后的URL
url = 'https://s.taobao.com/search?q='+r.quote(keyword)+'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc='+ r.quote(place) +'&ajax=true'
#itemList = []
def reqTimeOut(url,timeOut):
#    fileURL = open('reqUrl.txt','a+',encoding='utf-8')
    filename = keyword + '在' + place + '.txt'
    fileList = open(filename,'a+',encoding='gbk')
    for i in range(0,100):
        urlPage = url + '&s=' + str(i*44)
        f= r.urlopen(urlPage)
        if f.getcode() == 200 :
            data = f.read().decode('utf-8','ignore')
        else:
            print('网络请求错误,正在重试中。。。')
            i = i-1
        data = json.loads(data)
        data = json.dumps(data['mods']['itemlist']['data']['auctions'])
#        try:
#            fileURL.write(urlPage+'\n')
#        except Exception as err:
#            print('文件写入URL错误！重试中。。。')
#            continue
        try:
            fileList.write(data + '\n')
        except Exception as err:
            print('文件写入Data错误！重试中。。。')
            continue
#        itemList.append(data['mods']['itemlist']['data']['auctions'])
        print('爬取关键词'+keyword+'在城市'+place+'的第'+str(i+1)+'页成功！')
        time.sleep(timeOut)
#    fileURL.close()
    fileList.close()

#运行爬取数据的函数
reqTimeOut(url,0)