#-*- codeing = utf-8 -*-
#@Time: 2020/12/1 21:34
#@Author: Wang Wei
#@File: testXlwt.py
#@Software: PyCharm


import xlwt

# wookbook = xlwt.Workbook(encoding='utf-8')  #创建workbook对象
# worksheet = wookbook.add_sheet('sheet1')    #创建工作表
# worksheet.write(0,0,'hello,world')          #写入数据，行，列，内容
# wookbook.save('student.xls')               #保存数据表

wookbook = xlwt.Workbook(encoding='utf-8')  #创建workbook对象
worksheet = wookbook.add_sheet('sheet1')

for i in range(0,10):
    for j in range(0,i+1):
        worksheet.write(i,j,'%d * %d = %d'%(i,j,i*j))
wookbook.save('student.xls')