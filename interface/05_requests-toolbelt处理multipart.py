# encoding: utf-8

from requests_toolbelt import MultipartEncoder
import requests

host='http://112.74.112.220:8083'#禅道服务器地址

def login(s,user="laraine",psw="e10adc3949ba59abbe56e057f20f883e"):
    u"登录禅道"
    loginUrl=host+"/user-login.html"
    h={
        "Connection":"keep-alive",
        "Content-Length":"120",
        "Cache-Control":"max-age=0",
        "Origin":"http://112.74.112.220:8083",
        "Upgrade-Insecure-Requests":"1",
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Referer":"http://112.74.112.220:8083/user-login.html",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"en,zh-CN;q=0.9,zh;q=0.8",

    }

    boby={
        "account":user,
        "password":psw,
        "Referer":host+"/my/"
    }

    try:
        r=s.port(loginUrl,data=boby,hearder=h)
        print(r.content)#打印结果看到location=‘host+"/my/"说明登录成功了
        if "/my/in r.content":
            print("登录成功了")
            return True
        else:
            print("登录失败：%s"%r.content)
            return False
    except Exception as msg:
        print("登录失败：%s"%str(msg))
        return False

    # def upload_jpg(s):
    #     u"上传图片"
    #     url=












