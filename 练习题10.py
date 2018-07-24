# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:23:53 2018

@author: 虞姬1987
"""
#（高考派数据获取方式）练习题10：
#1.获取2300所学校的编号
#2.获取31所城市的编号
#3.获取142000数据，31/10，每个组有三个城市数据，后面组装在一起
#4.将142600数据使用spark统计

#获取高校ID列表，并存储在allSchoolId.txt文件中 
#import re
import json
import urllib.request as r
def writeInfo(dictData,flieName,TYPE,ENCODE):
    try:
        #打开文件
        file = open(flieName,TYPE,encoding=ENCODE)
        #将字典dictData转化为str
        str = json.dumps(dictData)
        #写入文件，将数据放置缓存区中
        file.write(str + '\n')
        #关闭文件，将缓存区数据写入文件，关闭文件
        file.close()
    except Exception as err:
        print('文件写入dictData错误！')
"""
schoolId = {}
fileSchoolId = open('all_school.txt','r',encoding='utf-8')
#循环读取文件每一行
while True:
    lines = fileSchoolId.readline() # 整行读取数据
    #为空行则遍历文件结束，退出循环
    if not lines:
        break
    try:
        strSchool = re.findall(u"[\u4e00-\u9fa5]+|[0-9]\d*",lines)[0]
        strSchoolId = re.findall(r"[0-9]\d*",lines)[0]
        schoolId[strSchoolId] = strSchool
    except Exception as err:
        print('该行查询失败，重试中。。。')
        continue
fileSchoolId.close()
#将数据写入allSchoolId.txt文件中
writeInfo(schoolId,'allSchoolId.txt','a+','utf-8')
"""
#获取学校，放到schoolList列表中
fileSchoolId = open('allSchoolId.txt','r',encoding='utf-8')
data = json.loads(fileSchoolId.readline())
lenData = len(data)
schoolIdList = list(data.keys())
fileSchoolId.close()
#获取城市，放到cityList列表中
#cityId = [35,36,37]
#cityId = [11]
#这是主进程，为了提高性能后期选择多线程
url= 'http://www.gaokaopai.com/university-ajaxGetMajor.html' 

    #请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'}
#f=open('全国招生人数.txt','a+',encoding='utf-8')
for schoolid in schoolIdList:
    f=open('江西招生人数.txt','a+',encoding='utf-8')
    for kemu in [1,2]:
        req=r.Request(url,data='id={}&type={}&city=36&state=1'.format(schoolid,kemu).encode(),headers=headers)
        f.write(r.urlopen(req).read().decode('utf-8','ignore')+"\n")
    print(schoolid+"数据获取成功！")
    f.close()
print('数据获取完成！')

