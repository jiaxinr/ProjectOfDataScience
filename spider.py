import requests
import bs4
import os
import datetime
import time
from urllib import  request
import urllib.request
import re
def findMax(list):
    max = 0
    for i in list:
        if i > max:
            max = i
    return max

def fetchUrl(url):

    #函数用来获取目标网页的html内容
    headers ={
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    r = requests.get(url, headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
    # req = urllib.request.Request(url, headers=headers)
    # response = urllib.request.urlopen(req)
    # html = response.read().decode('utf-8')
    # return html

def getPageList(year, month, day):
    #获取当天报纸各版面的链接列表
    url = 'http://paper.people.com.cn/rmrb/html/'+ year + '-' + month + '/' + day +'/nbs.D110000renmrb_01.htm'
    html = fetchUrl(url)
    bs = bs4.BeautifulSoup(html, 'html.parser')
    pageList = bs.find('div', attrs = {'id': 'pageList'}).ul.find_all('div', attrs = {'class': 'right_title-name'})
    linkList = []

    for page in pageList:
        link = page.a["href"]
        url = 'http://paper.people.com.cn/rmrb/html/'+ year + '-' + month + '/' + day + '/'+ link
        linkList.append(url)

    return linkList

def getTitleList(year, month, day, pageurl):
    #获取报纸某一版面的文章链接列表
    html = fetchUrl(pageurl)
    bs = bs4.BeautifulSoup(html, 'html.parser')
    titleList = bs.find('div', attrs={'id':'titleList'}).ul.find_all('li')
    linkList = []

    for title in titleList:
        tempList = title.find_all('a')
        for temp in tempList:
            link = temp["href"]
            if 'nw.D110000renmrb' in link:
                url = 'http://paper.people.com.cn/rmrb/html/' + year + '-' + month + '/' + day + '/' + link
                linkList.append(url)

    return linkList


def getContent(html):
    #解析html网页，获取新闻的文章内容
    bs = bs4.BeautifulSoup(html, 'html.parser')
    #获取文章标题,h3和h1分别是html文件里面的属性
    mainTitle= bs.h1.text
    mainTitle = str(mainTitle)

    #目前暂时还不知道如何把几个正则表达式写到一个列表里，就是用多个正则表达式去处理标题
    Kwords1 = re.compile(r'(.*)疫情(.*)')
    Kwords2 = re.compile(r'(.*)新冠(.*)')
    Kwords3 = re.compile(r'(.*)新型冠状(.*)')
    KwordsList = []
    KwordsList.append(Kwords1)
    KwordsList.append(Kwords2)
    KwordsList.append(Kwords3)

    #findKwords = re.compile(r'(.*)疫情(.*)')
    lengthList = []
    for findKwords in KwordsList:
        lengthList.append(len(re.findall(findKwords, mainTitle)))    #分别用每一个正则表达式去匹配标题，并且把匹配之后返回的长度存在一个列表里

    if findMax(lengthList) > 0:
        title = bs.h3.text + '\n' + bs.h1.text + '\n' + bs.h2.text + '\n'
        # print(title)
        plist = bs.find('div', attrs={'id': 'ozoom'}).find_all('p')
        content = ""
        for p in plist:
            content += p.text + '\n'
        resp = title + content
        return resp
    #如果没有一个关键词是符合的
    return "This is the file that doesn't fits our need!"


def saveFile(content, path, filename):
    if content != "This is the file that doesn't fits our need!":
        #如果content的内容不是我们想要的，就将文章内容content保存到本地文件中
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + filename , 'w', encoding = 'utf-8') as f:
            f.write(content)

def download_rmrb(year, month, day, destdir):
    #爬取人民日报网站某年某月某日的新闻内容并保存在指定目录下
    pageList = getPageList(year, month, day)    #获得版面的集合
    for page in pageList:        #对于每一个版面，获取每一个标题
        titleList = getTitleList(year, month, day, page)
        for url in titleList:     #对于每一个标题的url链解，点进去获取每一个的内容
            html = fetchUrl(url)
            content = getContent(html)

            #生成保存的文件路径以及文件名
            temp = url.split('_')[2].split('.')[0].split('-')
            pageNo = temp[1]     #获取版面号
            titleNo = temp[0] if int(temp[0]) >= 10 else '0' + temp[0]
            path = destdir + '/' + year + month + day + '/'
            fileName = year + month + day + '-' + pageNo + '-' + titleNo + '.txt'

            # 保存文件
            saveFile(content, path, fileName)

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



if __name__ == '__main__':
    beginDate = input('请输入开始日期（格式如20190502）：')
    endDate = input('请输入结束日期：')
    data = get_data_list(beginDate, endDate)

    for d in data:
        year = str(d.year)
        month = str(d.month) if (d.month >= 10) else '0' + str(d.month)
        day = str(d.day) if (d.day >= 10) else '0' + str(d.day)
        download_rmrb(year, month, day, 'data')
        print("爬取完成：" + year + month + day)
