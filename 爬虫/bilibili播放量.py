from bs4 import BeautifulSoup
import urllib.request,urllib.error
import xlwt
import sqlite3
import re
import requests
import pandas as pd
import re
import time
import json
import random
from concurrent.futures import ThreadPoolExecutor
import datetime


def download_page(url):
    """
    下载页面
    :param url: 页面请求地址
    :return: 请求响应的 response
    """
    # 配置请求头
    # User-Agent：浏览器代理（把自己伪装成浏览器请求）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers)
    return res

def getcid(BV):
    av = BV.strip('BV')
    #"https://api.bilibili.com/x/player/pagelist?bvid=BV1NE411w7TF&jsonp=jsonp"
    url = f'https://api.bilibili.com/x/player/pagelist?bvid={BV}&jsonp=jsonp'
    res = download_page(url)
    res_text = res.text
    #print(res_text)
    res_dict = json.loads(res_text)
    cid = res_dict['data'][0]['cid']
    #print(cid)
    return cid

start_time = datetime.datetime.now()
oidnow='128777652'

def Grab_barrage(bv):
    # 伪装请求头
    headers = {
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "origin": "https://www.bilibili.com",
        "referer": "https://www.bilibili.com/video/BV1Z5411Y7or?from=search&seid=8575656932289970537",
        "cookie": "_uuid=8393E73A-4EDC-7DDC-8847-6B6B5725000281522infoc; buvid3=62CA8CF3-B050-439E-B517-EB781D06418E155839infoc; LIVE_BUVID=AUTO4615858219391929; rpdid=|(um)~|m|mk|0J'ul)l)kumR|; sid=cfpndph7; blackside_state=1; CURRENT_FNVAL=80; CURRENT_QUALITY=80; DedeUserID=477652162; DedeUserID__ckMd5=7234abf76c96ad59; SESSDATA=75c168b2%2C1622357881%2Ce9cea*c1; bili_jct=d3b47a304245bb227d150e7a8c268639; bsource=search_baidu; bp_video_offset_477652162=469085156862671080; PVID=3; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f",
        "user-agent": random.choice(user_agent),
    }
    # 构造url访问   需要用到的参数

    # 发送请求  获取响应

    urlcomment="https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid="+str(oidnow)+"&sort=2"
    #print(urlcomment)
    request = urllib.request.Request(urlcomment, headers=headers)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    findcomment=re.compile(r'"message":(.*?),')
    link = re.findall(findcomment,html)
    #print(link)
    # 将每条弹幕数据写入txt
    filename="numbers.txt"
    with open(filename, 'a+') as f:
        f.write(oidnow+"\n")
        f.write(bv+"\n")
        #print(oidnow)
        for con in link:
            try:
                #print(con)
                f.write(con+"\n")
            except UnicodeEncodeError as e:
                pass

    time.sleep(random.randint(1, 3))  # 休眠
    delta = (datetime.datetime.now() - start_time).total_seconds()
    print(f'用时：{delta}s')





table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr = {}
for i in range(58):
    tr[table[i]] = i
s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608


def bv2av(x):
    r = 0
    for i in range(6):
        r += tr[x[s[i]]] * 58 ** i
    return (r - add) ^ xor

"""
以上算法转载自
如何看待 2020 年 3 月 23 日哔哩哔哩将稿件的「av 号」变更为「BV 号」？ - mcfx的回答 - 知乎
https://www.zhihu.com/question/381784377/answer/1099438784
"""


def avbv_exc(data):
    if 'BV' in data:
        p = r'(BV[a-zA-Z0-9]{10})'
    bvid = re.findall(p, data)[0]
    id = bv2av(bvid)
    return id

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

headers = {   #cookie要换成自己的
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "origin": "https://www.bilibili.com",
        "referer": "https://www.bilibili.com/video/BV1Z5411Y7or?from=search&seid=8575656932289970537",
        "cookie": "_uuid=8393E73A-4EDC-7DDC-8847-6B6B5725000281522infoc; buvid3=62CA8CF3-B050-439E-B517-EB781D06418E155839infoc; LIVE_BUVID=AUTO4615858219391929; rpdid=|(um)~|m|mk|0J'ul)l)kumR|; sid=cfpndph7; blackside_state=1; CURRENT_FNVAL=80; CURRENT_QUALITY=80; DedeUserID=477652162; DedeUserID__ckMd5=7234abf76c96ad59; SESSDATA=75c168b2%2C1622357881%2Ce9cea*c1; bili_jct=d3b47a304245bb227d150e7a8c268639; bsource=search_baidu; bp_video_offset_477652162=469085156862671080; PVID=3; bfe_id=fdfaf33a01b88dd4692ca80f00c2de7f",
        "user-agent": random.choice(user_agent),
    }


urlOfNumbers="http://api.bilibili.com/archive_stat/stat?aid="
url="https://search.bilibili.com/all?keyword=%E7%96%AB%E6%83%85&page=" #b站搜索栏搜索关键词复制下来的链接，我这个是“疫情”，建议大家换一下
data=[]

for i in range(20,51):    #第几页到第几页，建议换一下，换了关键词之后从第一页开始，或者不换关键词从后面一点开始
    html = ""
    newurl=url+str(i)
    request = urllib.request.Request(newurl, headers=headers)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    soup = BeautifulSoup(html, "html.parser")
    #print(soup)

    findbvid = re.compile(r'"bvid":"(.*?)"')

    for item in soup.find_all():  # 查找所有符合要求的
        data = []
        item = str(item)
        link = re.findall(findbvid, item)
        cnt=0
        if (len(link)):
            for bv in link:
                oidnow=str(avbv_exc(bv))
                Grab_barrage(bv)
        break
