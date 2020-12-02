#-*- codeing = utf-8 -*-
#@Time: 2020/10/20 19:38
#@Author: Wang Wei
#@File: spider01.py
#@Software: PyCharm

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    print(datalist)
    savepath = "豆瓣电影Top250.xls"
    #getData(baseurl)
    saveData(datalist,savepath)
    askURL(baseurl)

#匹配电影链接
findLink = re.compile(r'<a href="(.*?)">')
#匹配图片链接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)  #re.S 让换行符包含在字符中
#匹配电影名
findName = re.compile(r'<span class="title">(.*)</span>')
#匹配评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#匹配评分人数
findRatingNum = re.compile(r'<span>(\d*)人评价</span>')
#匹配电影概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#匹配电影相关信息
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


#这个函数只能爬25条数据，不知道问题出在哪？？？？
#爬取网页
# def getData(baseurl):
#     datalist = []
#     for i in range(0, 10):
#         url = baseurl + str(i * 25)
#         html = askURL(url)  #保存获取到的网页源码
#
#     #2.逐一解析数据
#     soup = BeautifulSoup(html, 'html.parser')
#     for item in soup.find_all('div', class_="item"):
#         #print(item)
#         data = []       #保存一部电影信息
#         item = str(item)
#
#
#         movielink = re.findall(findLink, item)[0]
#         data.append(movielink)
#
#         picLink = re.findall(findImgSrc, item)[0]
#         data.append(picLink)
#
#         movieName = re.findall(findName, item)   #片名可能只有一个中文名
#         if (len(movieName) == 2):
#             ctitle = movieName[0]
#             data.append(ctitle)
#             ftitle = movieName[1].replace("/", "")   #去掉无关符号
#             data.append(ftitle)
#         else:
#             data.append(movieName[0])
#             data.append(" ")      #为外文名留空留空
#
#
#         rating = re.findall(findRating, item)[0]
#         data.append(rating)
#
#         ratingNum = re.findall(findRatingNum, item)[0]
#         data.append(ratingNum)
#
#
#         #添加电影概况
#         inq = re.findall(findInq, item)
#         if len(inq) != 0:
#             inq = inq[0].replace("。", "")  #去掉句号
#             data.append(inq)
#         else:
#             data.append(" ")
#
#         #添加电影相关信息
#         bd = re.findall(findBd, item)[0]
#         bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
#         bd = re.sub('/', " ", bd)
#         data.append(bd.strip())    #去掉前面空格
#
#
#         datalist.append(data)
#
#     #print(datalist)
#     return datalist

def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)   #测试：查看电影item全部信息
            data = []  # 保存一部电影的所有信息
            item = str(item)

            # 影片详情的链接
            link = re.findall(findLink, item)[0]  # re库用来通过正则表达式查找指定的字符串
            data.append(link)  # 添加链接

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)  # 添加图片

            titles = re.findall(findName, item)  # 片名可能只有一个中文名，没有外国名
            if (len(titles) == 2):
                ctitle = titles[0]  # 添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去掉无关的符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ')  # 外国名字留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加评分

            judgeNum = re.findall(findRatingNum, item)[0]
            data.append(judgeNum)  # 提加评价人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格

            datalist.append(data)  # 把处理好的一部电影信息放入datalist

    return datalist



#得到指定一个URL的网页内容
def askURL(url):
    header = {              #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
    }                       #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
    req = urllib.request.Request(url, headers=header)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
#3.保存数据
def saveData(datalist,savepath):
    wookbook = xlwt.Workbook(encoding='utf-8',style_compression=0)
    worksheet = wookbook.add_sheet('sheet1',cell_overwrite_ok=True)
    col = ("电影链接","图片链接","电影中文名","电影外文名","评分","评分人数","电影概况","相关信息")
    for i in range(0,8):
        worksheet.write(0,i,col[i])   #列名
    for i in range(0,250):
        data = []
        while '' in data:
            data.remove('')
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])   #数据

    wookbook.save(savepath)      #保存


if __name__ == '__main__':
    main()
    print("爬取完毕！")