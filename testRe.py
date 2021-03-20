#-*- codeing = utf-8 -*-
#@Time: 2020/10/22 22:03
#@Author: Wang Wei
#@File: testRe.py
#@Software: PyCharm



import re

#创建模式对象

#complie用来校验其他字符串中是否有AA
# pat = re.compile("AA")
# m = pat.search("ABCAA")
# print(m)

#与上面的compile效果一样，前面字符串是规则（正则表达式），后面的是字符串
#m = re.search("asd","Aasd")

#print(re.findall("a","abcsdfsdaaa"))
# print(re.findall("[A-Z]","ABCsdfsdaaa"))
#print(re.findall("[A-Z]+","ABCsdfsdaaa"))
# #print(m)

#sub   在第三个字符串中找到a用A替换
#print(re.sub('a','A','absdaew'))

#建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
# a = r"\aabd-\'"
# print(a)

list = ['<span class="jname at" title="Python开发工程师">Python开发工程师</span>', '<span class="time">03-20发布</span>', '<span class="sal">1.5-2万/月</span>', '<span class="d at">大连  |  5-7年经验  |  本科  |  招1人</span>', '<span><i>五险一金</i><i>弹性工作</i><i>补充医疗保险</i><i>定期体检</i></span>', '<span class="jname at" title="Python开发工程师">Python开发工程师</span>']

findJob = re.compile(r'<span class="jname at" title="(.*)">')

#item = bs.select(".e > a > p > span")
for i in list:
        print(re.findall(findJob, i))
