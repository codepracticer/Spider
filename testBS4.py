#-*- codeing = utf-8 -*-
#@Time: 2020/10/20 21:21
#@Author: Wang Wei
#@File: testBS4.py
#@Software: PyCharm
# 上次看到 21 集

from bs4 import BeautifulSoup

file = open("./baidu.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")


#1.Tag标签及其内容 ， 默认只拿到它所找到的第一个内容
# print(bs.title)
# print(bs.a)
# print(bs.head)

#2.NavigableString   标签里的内容（字符串）
# print(bs.title.string)
# print(bs.a.attrs)

#3.BeautifulSoup  表示整个文档
#print(type(bs))  #BeautifulSoup

#4.Comment   是一个特殊的NavigableString ，输出的内容不包含注释符号
# print(bs.a.string)
# print(type(bs.a.string))xcb


#文档搜索
#t_list = bs.find_all("a")

import re
#正则表达式搜索：使用search（）方法来匹配内容
# t_list = bs.find_all(re.compile("a"))

#方法： 传入一个函数，根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)


#kwargs  参数
# t_list = bs.find_all(id="username")
#t_list = bs.find_all(class_=True)

#3.text参数
#t_list = bs.find_all(text=["新闻",'地图','hao123'])
#t_list = bs.find_all(text=re.compile("\d"))  #应用正则表达式来查找包含特定文本的内容

#4.limit 参数
#t_list = bs.find_all("a",limit=3)

#css 选择器
#t_list = bs.select(".div_menu")  #通过类选择器来选择
#t_list = bs.select("#ww")    #通过id选择器来选择

#t_list = bs.select("a[class='']")  #通过属性来查找

#t_list = bs.select("head > title")  #通过子标签来查找

#t_list = bs.select(".div_menu ~ .div_")  #通过兄弟/同级标签来查找


#print(t_list[0].get_text())
for item in t_list:
    print(item)
