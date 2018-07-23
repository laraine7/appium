# encoding: utf-8

import requests
import urllib3
urllib3.disable_warnings()#可以屏蔽warring错误提示信息

#先打开登录首页，获取部分cookie
#通过session保存cookie，模拟登陆

url="https://passport.cnblogs.com/user/signin"
method="get"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Cookie":"UM_distinctid=160a03a6d252a3-01cfe031b18d37-5d153916-1fa400-160a03a6d27e; _ga=GA1.2.1649791209.1516246258; __gads=ID=c86d27c79562ba45:T=1525250433:S=ALNI_MY_FTZq0o2QslAcY8xKWAQXyyEFdw; _gid=GA1.2.714839364.1529638189; _gat=1; ASP.NET_SessionId=0honnmo1yfizma5mola0dheq; SERVERID=34e1ee01aa40e94e2474dffd938824db|1529638183|1529638182",

}

#增加
params=""
boby=""
verify=False
s=requests.session()
# r=s.request(method=method, url=url,headers=headers,verify=False)
r=s.request(method=method,url=url,params=params,headers=headers,data=boby,verify=verify)


print(r.cookies)
print(r.text)
#
# #添加登录需要的两个cookie
# #更新
# c = requests.cookies.RequestsCookieJar()#定义一个cookie对象
#
# c.set('.CNBlogsCookie','F5BA54B8E27F674946470162AC1D0032EABB3D532EB9FC63F4E4CBAD7A0A55FD31F51D3364435E9193611266336AD9215108A8A3CED90FD220203D0A67138D127E7BCD29148AF817BA1DA6E6CFD33C28593DD037; domain=.cnblogs.com; path=/; HttpOnly')
# c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8FHXRRtkJWRFtU30nh_M9mCf8gLYJBVjiC9tZnl6tuixg5Q1HSumoKp9KcCb4AdKiCYywUVdE_UVKlKZnYmcIUR0kznnlT9-skNTvNAvadgrShjzdSuVWlTt6jIkhNLqsqpTzNcPiGrJzUUF_JN1u8aKbbwSx_vIiazXaFRmPA2tU9D6DZRkZIuERka_n_swewsJsP-z7feyv5WwiR25BoQaKrLJbol1_BXmB484cK7pUwWrHCxzD8bX4VyZa64saVoGl3FgE5PMskb8t7ULy1Tu1xIJi-u6gjX8H3SHawBG; domain=.cnblogs.com; path=/; HttpOnly')
# #由于博客园的登录机制变了，这里需要多添加两个cookie
# c.set('AlwaysCreateItemsAsActive',"True")
# c.set('AdminCookieAlwaysExpandAdvanced',"True")
# s.cookies.update(c)#更新S的cookie
#
# # print(s.cookies)
#
# #登录成功后保存编辑内容
# r1=s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1",headers=headers,verify=False)
#
#
# #保存草稿
# url2="https://i.cnblogs.com/EditPosts.aspx?opt=1"
# # r1=s.get(url2,headers=headers,verify=False)
#
# boby={"__VIEWSTATE":"",
#       "__VIEWSTATEGENERATOR":"FE27D343",
#       "Editor$Edit$txbTitle":"我就坎坎坷坷",
#       "Editor$Edit$EditorBody":"有什么区别",
#       "Editor$Edit$Advanced$ckbPublished":"on",
#       "Editor$Edit$Advanced$chkDisplayHomePage":"on",
#       "Editor$Edit$Advanced$chkComments":"on",
#       "Editor$Edit$Advanced$chkMainSyndication":"on",
#       "Editor$Edit$Advanced$txbEntryName":"",
#       "Editor$Edit$Advanced$txbExcerpt":"",
#       "Editor$Edit$Advanced$txbTag":"",
#       "Editor$Edit$Advanced$tbEnryPassword":"",
#       "Editor$Edit$lkbDraft":"存为草稿"
#       }
#
#
# r2=s.post(url2,data=boby,verify=False)
#
# print(r2.url)

# url="https://i.cnblogs.com/PostDone.aspx?postid=9289937&actiontip=%e5%ad%98%e4%b8%ba%e8%8d%89%e7%a8%bf%e6%88%90%e5%8a%9f"
# import re
# postid=re.findall(r"postid=(.+?)&",url)
# print(postid)
#
# print(postid[0])

# print(r.text)








