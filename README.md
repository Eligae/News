# News
## NAVER PAPAGO API
[사용방법 예시](https://developers.naver.com/docs/papago/papago-nmt-example-code.md#python)

```python
import os
import sys
import urllib.request
client_id = "YOUR_CLIENT_ID" # 개발자센터에서 발급받은 Client ID 값
client_secret = "YOUR_CLIENT_SECRET" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote("반갑습니다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
```
## 설명
```main.py```에서 실행하면, ```loginWindow.py```에서 login을 확인하고, ```NewsWindow.py```를 띄워 뉴스에 대해 분석합니다. 