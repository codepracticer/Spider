#-*- codeing = utf-8 -*-
#@Time: 2020/10/22 22:03
#@Author: Wang Wei
#@File: testRe.py
#@Software: PyCharm



import re

#创建模式对象

#complie用来校验其他字符串中是否有AA
# # pat = re.compile("AA")
# # m = pat.search("ABCAA")

#与上面的compile效果一样，前面字符串是规则（正则表达式），后面的是字符串
#m = re.search("asd","Aasd")

#print(re.findall("a","abcsdfsdaaa"))
# print(re.findall("[A-Z]","ABCsdfsdaaa"))
#print(re.findall("[A-Z]+","ABCsdfsdaaa"))
# #print(m)

#sub   在第三个字符串中找到a用A替换
print(re.sub('a','A','absdaew'))

#建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
a = r"\aabd-\'"
print(a)
