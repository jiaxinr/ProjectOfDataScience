import math

import requests
import bs4
import os
import datetime
import time
from urllib import  request
import urllib.request
import re

import urllib3

urllib3.disable_warnings()
global starcaltime
global endcaltime

def fetchUrl(url):

    #函数用来获取目标网页的html内容
    headers ={
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    try:
        r = requests.get(url, headers, verify = False)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except requests.exceptions.HTTPError:
        print("访问页面出错")
        time.sleep(2)


#这个方法用来获取所有的关键词
def getSearchList():
    global kw
    keywordList = ['新冠', '新型冠状', '疫情']
    # 获得一个搜索界面的列表
    # searchList = []
    for kword in keywordList:
        # searchList.append('https://so.jstv.com/?keyword=' + kword)
        url ='https://so.jstv.com/?keyword=' + kword
        #获得这个关键词的正则表达式
        kw = re.compile(r'(.*)' + kword + r'(.*)')
    # for url in searchList:
        getPageList(url, kw)


# 这个方法用来获取所有的页面
def getPageList(url, kw):
    try:
        html = fetchUrl(url)
        bs = bs4.BeautifulSoup(html, 'html.parser')
        resultMessage = bs.find('div', attrs={'class':'lzxw_l'}).p.string.lstrip()
        resultMessage = resultMessage.replace("为您找到相关结果约 ", "").replace("个", "").replace("\n","").replace("\t","").replace(",","")
        #获得每一个搜索结果下相关结果的条数
        resultNum = int(resultMessage)
        pageNum = math.ceil(resultNum / 10)
        #获取接下来的几页,倒序获取

        # for pageNo in range(2790, 2780, -1):
        for pageNo in range(pageNum, 0, -1):
            nowurl = url + '&page='+ str(pageNo)
            html = fetchUrl(nowurl)
            titlelist = getTitleList(html, kw)
            #每一个page的titleList都是完全符合我们要求的，所以获得该页的url加入page中
            for itemurl in titlelist:
                html = fetchUrl(itemurl)
                content = getContent(html)
                #分解url，获得日期
                urllist = itemurl.split('/')
                date = urllist[4]
                name = urllist[5].replace('.shtml','')
                destdir = 'data'
                path = destdir + '/' + date + '/'
                filename = date + '-' + name + '.txt'
                saveFile(content, path, filename)
                print("爬取完成：" + filename)
    except TypeError:
        print("TypeError")
        time.sleep(2)

def getTitleList(html, kw):
    bs = bs4.BeautifulSoup(html, 'html.parser')
    #每一页的10个（或者更少新闻的url放入一个list当中）
    titleList = bs.find('div', attrs={'class':'lzxw_lxz'}).ul.find_all('li')
    # titleList = bs.find('div', attrs={'class': 'lzxw_l'}).ul.find_all('li')
    linkList = []
    for title in titleList:
        tempList = title.find_all('a')
        for temp in tempList:
            title = str(temp)
            if len(kw.findall(title)) != 0:    #如果找到了元素
                link = temp["href"]
                tm = str(link).split('/')[4]
                year = tm[0:4]
                month = tm[4:6]
                day = tm[6:8]
                calcurrtime = timeTransfer(month, day)
                #判断时间是否符合要求,符合要求获得链接
                #暂时还没有传入时间，先设置一下
                if year == '2020' and starcaltime <= calcurrtime <= endcaltime:
                    linkList.append(link)

    return linkList

def getContent(html):
    bs = bs4.BeautifulSoup(html, 'html.parser')
    title = bs.find('div', attrs={'class': 'article'}).h3.text
    contentlist = bs.find('div', attrs={'class': 'content'}).find_all('p')
    content = ""
    for c in contentlist:
        content += c.text + '\n'
    resp = title + content
    return resp


def saveFile(content, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'w', encoding='utf-8') as f:
        f.write(content)

def gen_dates(b_date, days):
    day = datetime.timedelta(days = 1)
    for i in range(days):
        yield b_date + day * i

def get_data_list(beginDate, endDate):
    #传入两个参数：开始日期和结束日期，返回两个日期之间的日期列表
    start = datetime.datetime.strptime(beginDate, "%Y%m%d")
    end = datetime.datetime.strptime(endDate, "%Y%m%d")

    data = []
    for d in gen_dates(start, (end - start).days):
        data.append(d)

    return data


def timeTransfer(month, day):
    return int(str(month)) * 100 + int(str(day))

if __name__ == '__main__':
    # beginDate = input('请输入开始日期（格式如20190502）：')
    # endDate = input('请输入结束日期：')
    beginDate = '20200121'
    endDate = '20200722'
    # data = get_data_list(beginDate, endDate)
    beginmonth = beginDate[4:6]
    beginday = beginDate[6:8]
    endmonth = endDate[4:6]
    endday = endDate[6:8]
    starcaltime = timeTransfer(beginmonth, beginday)
    endcaltime = timeTransfer(endmonth, endday)
    getSearchList()
    # for d in data:
    #     year = str(d.year)
    #     month = str(d.month) if (d.month >= 10) else '0' + str(d.month)
    #     day = str(d.day) if (d.day >= 10) else '0' + str(d.day)
    #
    #     print("爬取完成：" + year + month + day)










