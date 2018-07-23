# encoding: utf-8

from bs4 import BeautifulSoup
import requests

# r=requests.get("http://www.cnblogs.com/yoyoketang/")
# #请求首页后获取整个html界面
#
# blog=r.content
# #用html.parser解析html
# soup=BeautifulSoup(blog,"html.parser")
# #获取所有class属性为“dayTitle”，返回tag类
# # times=soup.find_all(class_="postTitle")
# # for i in times:
# #     a=i
# #     print( i.a.string)#获取a标签的文本
#
# descs=soup.find_all(class_="postCon")
# for i in descs:
#     c=i.div.contents[0]
#     print(c)
#
# lee=open("lee-h.html",encoding='gbk',errors='ignore')
# print(lee.read())

# soup=BeautifulSoup(lee,"html.parser")
# print(soup.prettify())#这个方法是把文件解析成html格式,用html的保准格式输出
# print(type(soup))
# print(soup)

# tag=soup.title
# print(type(tag))
# print(tag)

# string=soup.p.string
# print(type(string))
#
# print(string)
#
# comment=soup.b.string
# print(type(comment))
# print(comment)



#爬糗事百科的段子
# r=requests.get("https://www.qiushibaike.com/")
#
# qiubai=r.content
#
# soup=BeautifulSoup(qiubai,"html.parser")
# duanzi=soup.find_all(class_="content")
#
# for i in duanzi:
#     duan=i.span.contents[0]
#     print(duan)


import os

r=requests.get("http://699pic.com/people.html")
fengj=r.content
soup=BeautifulSoup(fengj,"html.parser")

images=soup.find_all(class_='lazy')

for i in images:
    jpg_rl=i["data-original"]
    title=i["title"]
    print(title)
    print(jpg_rl)
    print("")

    with open(os.getcwd()+"\\jpg\\"+title+'.jpg',"wb") as f:
        f.write(requests.get(jpg_rl).content)











