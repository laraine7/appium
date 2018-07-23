# encoding: utf-8

import requests
import json

#python的字典

# payload={"yoyo":True,
#          "Json":False,
#          "Python":"56546464",
#          }
#
# print(type(payload))
# print(payload)
#
# #转换为json格式
#
# data_json=json.dumps(payload)
# print(type(data_json))
# print(data_json)

#json数据处理

url="https://hdgateway.zto.com/WayBill_GetDetail"

headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",

}
d={
    "billCode":"211803543109"
}
s=requests.session()
r=s.post(url,headers=headers,data=d,verify=False)

# c = requests.cookies.RequestsCookieJar()#定义一个cookie对象
#
# c.set('ESG_OWF_NGINX_CNSZ17','ESG_OWF_CNSZ17_NGINX_WEB_226_131; Path=/')
#
# c.set('AlwaysCreateItemsAsActive',"True")
# c.set('AdminCookieAlwaysExpandAdvanced',"True")
# s.cookies.update(c)#更新S的cookie

# r=s.get(url,headers=headers,verify=False)

result=r.json()
# print(result)
data=result["result"]["logisticsRecord"]#获取result["result"]["logisticsRecord"]里面的内容
# print(data)
print(data[0][0])#获取result第一个
get_result=data[0][0]['stateDescription']
print(get_result)
if u"拍照签收"in get_result:
    print("快递单已签收成功")
else:
    print("签收失败")









