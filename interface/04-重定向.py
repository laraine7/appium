# encoding: utf-8

import requests
import urllib3
urllib3.disable_warnings()

url="https://i.cnblogs.com/EditPosts.aspx?opt=1"

headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

}

s=requests.session()
r=s.get(url,headers=headers,verify=False,allow_redirects=False)

print(r.status_code)
print(r.headers["Location"])

