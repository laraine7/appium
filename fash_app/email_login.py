# encoding: utf-8
import requests
import urllib3
urllib3.disable_warnings()




headers={
"User-Agent": "FashionTech/2.8.14 (iPhone; iOS 11.4; Scale/2.00)"

}

data={

    "callee":"FT_Server",
    "caller":"FT_iOS",
    "data":{
        "username":"1037791044@qq.com",
        "password":"VLMFB6UFRHqsZ9jWxiS3SCXbF4DfiknqMGJrbd1Sjd9ABAAxJ9Mo9I4LIvra5Zffuuf0R0MONAnqcZLhWkzfsSJmrpZOLOwl/dUgQ2N0/tzDwWY4i8ZeGmm0LdFNLjvv+DkCh38liYGJSEFfu8On/ALuaEEuRUMNuBHwsb++J0Y=",
        "deviceToken":"e82998cd f1c13620 db2b9bf3 14511031 b0ffccf8 9626cc2b 75ea88bb 09eb791a",
        "wallet_hash":""},
    "time":"1531218603",
    "token":"8ba4e18793ceefa3938b330693158ea7",

}

url="http://47.52.5.150:8083/api/mMember/login/"

s=requests.session()
r=s.post(url,json=data,headers=headers,verify=False)

print(r.text)
print(r.json())