#-*- codeing=utf-8 -*-

import re
from bs4 import BeautifulSoup
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseURL1="https://search.tianya.cn/bbs?q=%E7%96%AB%E6%83%85&pn="
    baseURL2="&s=2&f=3"
    dataList=getData(baseURL1,baseURL2)
    savePath="tianya1.xls"
    print("hhhhhhhhhhhhhhh")
    saveData(dataList,savePath)
    askURL("https://search.tianya.cn/bbs?q=%E7%96%AB%E6%83%85&pn=&s=2&f=3")
    #爬取网页、解析数据、保存数据

findLink=re.compile(r'" target="_blank">(.*?)<span class="kwcolor">(.*?)</span>(.*?)</a>',re.S)
findContent=re.compile(r'<p>(.*?)<span class="kwcolor">(.*?)</span>(.*?)</p>',re.S)


#爬取网页
def getData(baseURL1,baseURL2):
    dataList=[]
    for i in range(1,74):
        url=baseURL1+str(i)+baseURL2
        html=askURL(url)

        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find('div',class_="searchListOne").find_all('h3'):
            data=[]
            item=str(item)
            link=re.findall(findLink,item)[0]
            data.append(link)
            contentSrc=re.findall(findContent,item)[0]
            data.append(contentSrc)
            dataList.append(data)
    #print(dataList)
    return dataList

def askURL(url):
    head={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        reponse=urllib.request.urlopen(request)
        html=reponse.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html

#保存数据
def saveData(dataList,savePath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet('tianyaTry1',cell_overwrite_ok=True)
    col=("标题","正文")
    for i in range(0,2):
        sheet.write(0,i,col[i])
    for i in range(0,730):
        print("第%d条："%(i+1))
        data=dataList[i]
        for j in range(0,2):
            sheet.write(i+1,j,data[j])
    book.save('天涯数据1.xls')


if __name__ == '__main__':
    main()