#-*- codeing=utf-8 -*-
#author zzj
#date 2020/12/3




import xlrd
from bs4 import BeautifulSoup
import urllib.request,urllib.error
import xlwt
import sqlite3
import re
from xlutils.copy import copy

def main():
    #爬取网页 逐一解析数据 保存数据
    baseurl="https://news.baidu.com"
    datalist=getData(baseurl)
    savepath=".\\百度.xls"
    saveData(datalist,savepath)


findLink=re.compile(r'<a href="(.*?)">')   #创建正则表达式对象 这个是找链接
findImgsrc=re.compile(r'<img.*src="(.*?)"',re.S)
findTitle=re.compile(r'<span class="title">(.*)</span>')
getnews=re.compile(r'target="_blank">(.*?)</a>')

#爬取网页
def getData(baseurl):
    datalist=[]
    url=baseurl
    html=askURL(url)
    soup=BeautifulSoup(html,"html.parser")
    #print(soup.prettify())
    for item in soup.find_all():#查找所有符合要求的 class_="bold-item"

            data=[] #save one movie
            item=str(item)
            #print(item)

            titles=re.findall(getnews,item)
            if(len(titles)!=0 and len(titles[0])!=0):
                data.append(titles[0])
            if(len(data)!=0):
                datalist.append(data)#save all movie
                print(data)

    #print(datalist)
    return datalist


#得到指定一个url的网页内容
def askURL(url):
    head={
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 87.0.4280.67 Safari / 537.36 Edg / 87.0.664.47"
    } #用户代理 伪装浏览器

    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html




def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf- 8",style_compression=0)  # 创建workbook对象
    seet = book.add_sheet('doubantop250',cell_overwrite_ok=True)  # 创建工作表
    #xls=xlrd.open_workbook(savepath,formatting_info=True)
    #xlsc=copy(xls)
    #seet=xlsc.get_sheet(0)
    num= len(datalist)
    for i in range(0,num):
        data=datalist[i]
        seet.write(i,0,data)
    book.save(savepath)



main()