#-*- codeing = utf-8 -*-
#@Time: 2020/10/20 19:56
#@Author: Wang Wei
#@File: testUrllib.py
#@Software: PyCharm

import urllib.request
import urllib.parse

url = "http://www.douban.com"

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))

#post请求
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

#get请求
# try:
#     response = urllib.request.urlopen("http://httpbin.org/post",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

#response = urllib.request.urlopen("http://www.baidu.com")
#print(response.getheaders())
#print(response.getheader("Date"))

data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
}
req = urllib.request.Request(url=url,data=data,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

