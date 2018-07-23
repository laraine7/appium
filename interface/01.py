# encoding: utf-8

import requests
import json

#请求博客首页

# r = requests.get('http://www.cnblogs.com/laraine')

# 找找看搜索功能
# par={"keywords":"python"}
# headerre={"Content-Type":"text/html",
#           # "Cookie":" __gads=ID=c86d27c79562ba45:T=1525250433:S=ALNI_MY_FTZq0o2QslAcY8xKWAQXyyEFdw;",
#
#           "Cookie":"UM_distinctid=160a03a6d252a3-01cfe031b18d37-5d153916-1fa400-160a03a6d27e; _ga=GA1.2.1649791209.1516246258; __gads=ID=c86d27c79562ba45:T=1525250433:S=ALNI_MY_FTZq0o2QslAcY8xKWAQXyyEFdw; _gid=GA1.2.1955877534.1529396841; __utma=116942413.1649791209.1516246258.1529485723.1529485723.1; __utmz=116942413.1529485723.1.1.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/"
# }
# r = requests.get('http://zzk-s.cnblogs.com/s/blogpost',params=par,headers=headerre)
#
# print(r.status_code)
# print(r.url)
# print(r.encoding)
# print(r.headers)
# print(r.cookies)
# print(r.text)
# print(r.content)


# payload={"yoyo":"hello world",
#          "pythonQQ群":"226296743"
#          }
#
# #转化成json格式
# data_json=json.dumps(payload)
# r=requests.post('http://httpbin.org/post',data=data_json)
#
# print(r.text)

#博客园登录

# headers={
#         "Connection": "keep-alive",
#         "Content-Length": "555",
#         "Accept": "application/json, text/javascript, */*; q=0.01",
#         "Origin": "https://passport.cnblogs.com",
#         "X-Requested-With": "XMLHttpRequest",
#         # "VerificationToken": "@TokenHeaderValue()",
#         # "User-Agent":" Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
#         "Content-Type": "application/json; charset=UTF-8",
#         # "Referer": "https://passport.cnblogs.com/user/signin?ReturnUrl=http%3A%2F%2Fzzk-s.cnblogs.com%2Fs%2Fblogpost%3FKeywords%3Dhello",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
#         "Cookie": "UM_distinctid=160a03a6d252a3-01cfe031b18d37-5d153916-1fa400-160a03a6d27e; _ga=GA1.2.1649791209.1516246258; __gads=ID=c86d27c79562ba45:T=1525250433:S=ALNI_MY_FTZq0o2QslAcY8xKWAQXyyEFdw; _gid=GA1.2.1955877534.1529396841; ASP.NET_SessionId=pbx33urmbqtomwmvn2mub30k; SERVERID=34e1ee01aa40e94e2474dffd938824db|1529551609|1529548216",
#         }
#
# payload={"input1":"R5W2ZEwnZPS6Vm8MoxVYgC+4eedArEbr+2jXu4vO61EZ6Ty6n3pUCKuWk+ZsQNJ8GaNkJxiX8hB9x/IcCwtNRxtulueHn5uKknwlWW725+OZ2LgwOIhqm/8benH8K/U7Dvbg5SMkisM/RSK1zuqUzPEDzohhJWYGdUKkdrYBENI=",
#          "input2":"w2KgzFrS1djdvGiN6mXdYR/CGmCkzkk1gvFFBhItXkOU+bRsp6jNI7gh7RU9FghgICx/ffNzbiVEqZd+aU4roVtariwmAhSIfUAwwiXJeyPF4IR22/ic8P8bHEwMCTnmTcxsv1mTgVYEe3IK+9eNZRlf7pj5HSVy6xD70ytVcE0=",
#          "remember":"False"
#          }
#
# url="https://passport.cnblogs.com/user/signin"
# r=requests.post(url,json=payload,headers=headers,verify=False)
#
# print(r.json())


#git登录

# headers={
#         "Connection": "keep-alive",
#         "Content-Length": "181",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#         "Origin": "https://github.com",
#         # "X-Requested-With": "XMLHttpRequest",
#         # "VerificationToken": "@TokenHeaderValue()",
#         # "User-Agent":" Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
#         "Content-Type": "application/x-www-form-urlencoded",
#         # "Referer": "https://passport.cnblogs.com/user/signin?ReturnUrl=http%3A%2F%2Fzzk-s.cnblogs.com%2Fs%2Fblogpost%3FKeywords%3Dhello",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
#         "Cookie": "_octo=GH1.1.178854169.1499829616;_ga=GA1.2.1120327849.1499829616;_gat=1;tz=Asia%2FShanghai;logged_in=no;_gh_sess=c1R0dHphUmlqK213Q0VOL2JNWkFoUnhBbW1qWno2MlZCdkRxa3l1TWpIamt3NnhBREpCbC8xZzhyVm1XOXBOQWJ0SWZuVGgrbWJrTDV2V1EzVzNvY3duTXJwenkweVlCdmFSOEs2NTNmOTVoTngwdVhSMTBJRG5lQnJVRm1pVzlTSVA0N3NCeTdNNFZYTHhTeTZsMjdzWEZKOHlqSmg5SzB4WUNYa2JZbktjd2R2OU9HM1Z0RWlKNUxGR1dHVzFoeFVkd0ttRGtVQ2d2ODJ2TzhFdlp1b0Ivc0Qyc2Vxb04zMGVxWklJODNyYWsxaGsrNTBhSkJRQ3FWc0praVZQc01SUkJPdEZwSTlvTWtiT2syemFNVjJyVTJnbGRpMTVEdjZ3NkVBaUdMR0o3VU9OUnVtR095S1BoeEFkdmtEL1N0ajlxZk1ma042aDNnVkErNEZmT3BiUFRCTWhLRzRmaWgzUThJbkg3Sy9tbjlSM3RPVHpGZFR2dUR6Q0hqUTJPUllBUWE3a1ptR1prK2JkRWlFYXc3S1I5ZXBidFlGNTFXek1KbFJzcC9tZz0tLWg4MHFLaTN6WkxWUjNsd3JreUtJcGc9PQ%3D%3D--718c2a59a387d8a7913e68644495750bffa82a47;",
#         }
# # headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",}
#
# d={"authenticity_token":"8EYLK73MqaKnzhbA7CCk4eg+L/uvWDZSKis8swZJnIsPbOE+S+oec4L8UC/7rNbWTNkHbWJpjmUcqC75PYt3IA==",
#    "commit":"Sign in",
#    "login":"laraine7",
#    "password":"20160725a",
#    "utf8":"%E2%9C%93"
# }
# url="https://github.com/login"
#
# s=requests.session()
#
# r=s.post(url,headers=headers,data=d)
#
# print(r.status_code)
#
# print(r.content)


#jenkins登录
import re
headers={"User-Agent":":Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "Connection": "keep-alive",
        "Content-Length": "315",
        "Cache-Control": "max-age=0",
        "Origin": "http://localhost:8080",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
         # "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
         "Referer": "http://localhost:8080/login?from=%2F",
         "Accept-Encoding": "gzip, deflate, br",
         "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
         "Cookie": "jenkins-timestamper-offset=-28800000; screenResolution=1920x1080; JSESSIONID.60c58cbf=node010uekkvdmy2xp4q39vzk5rxyl5.node0"




         }

d={"from":"",
   "Jenkins-Crumb":"11b448cb13eb6a7b48a73e8f15ee0674",
   "j_password":"20160725a",
   "j_username":"laraine",
   "Submit":"log in",
   "json":{"j_username": "laraine",
           "j_password": "20160725a",
           "remember_me": False,
           "from": "/",
           "Jenkins-Crumb": "11b448cb13eb6a7b48a73e8f15ee0674"}

}
url="http://localhost:8080/j_acegi_security_check"

s=requests.session()

r=s.post(url,headers=headers,data=d)
# t=re.findall(r'<b>(.+?)</b>',r.content)
print(r.status_code)

print(r.text)
print(1111111111111111111111)
print(r.content)
# print(t[0])
# print(t[1])
































