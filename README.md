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
```
python
├─ DATA
│  ├─ IT
│  │  └─ 과학
│  │     ├─ 1.txt
│  │     ├─ 10.txt
│  │     ├─ 11.txt
│  │     ├─ 12.txt
│  │     ├─ 13.txt
│  │     ├─ 14.txt
│  │     ├─ 15.txt
│  │     ├─ 16.txt
│  │     ├─ 17.txt
│  │     ├─ 18.txt
│  │     ├─ 19.txt
│  │     ├─ 2.txt
│  │     ├─ 20.txt
│  │     ├─ 21.txt
│  │     ├─ 22.txt
│  │     ├─ 3.txt
│  │     ├─ 4.txt
│  │     ├─ 5.txt
│  │     ├─ 6.txt
│  │     ├─ 7.txt
│  │     ├─ 8.txt
│  │     └─ 9.txt
│  ├─ 경제
│  │  ├─ 1.txt
│  │  ├─ 10.txt
│  │  ├─ 11.txt
│  │  ├─ 12.txt
│  │  ├─ 13.txt
│  │  ├─ 14.txt
│  │  ├─ 15.txt
│  │  ├─ 16.txt
│  │  ├─ 17.txt
│  │  ├─ 18.txt
│  │  ├─ 19.txt
│  │  ├─ 2.txt
│  │  ├─ 20.txt
│  │  ├─ 21.txt
│  │  ├─ 22.txt
│  │  ├─ 23.txt
│  │  ├─ 24.txt
│  │  ├─ 25.txt
│  │  ├─ 3.txt
│  │  ├─ 4.txt
│  │  ├─ 5.txt
│  │  ├─ 6.txt
│  │  ├─ 7.txt
│  │  ├─ 8.txt
│  │  └─ 9.txt
│  ├─ 사회
│  │  ├─ 1.txt
│  │  ├─ 10.txt
│  │  ├─ 11.txt
│  │  ├─ 12.txt
│  │  ├─ 13.txt
│  │  ├─ 14.txt
│  │  ├─ 15.txt
│  │  ├─ 16.txt
│  │  ├─ 17.txt
│  │  ├─ 18.txt
│  │  ├─ 19.txt
│  │  ├─ 2.txt
│  │  ├─ 20.txt
│  │  ├─ 21.txt
│  │  ├─ 22.txt
│  │  ├─ 23.txt
│  │  ├─ 24.txt
│  │  ├─ 25.txt
│  │  ├─ 3.txt
│  │  ├─ 4.txt
│  │  ├─ 5.txt
│  │  ├─ 6.txt
│  │  ├─ 7.txt
│  │  ├─ 8.txt
│  │  └─ 9.txt
│  ├─ 생활
│  │  └─ 문화
│  │     ├─ 1.txt
│  │     ├─ 10.txt
│  │     ├─ 11.txt
│  │     ├─ 12.txt
│  │     ├─ 13.txt
│  │     ├─ 14.txt
│  │     ├─ 15.txt
│  │     ├─ 16.txt
│  │     ├─ 17.txt
│  │     ├─ 18.txt
│  │     ├─ 19.txt
│  │     ├─ 2.txt
│  │     ├─ 20.txt
│  │     ├─ 21.txt
│  │     ├─ 22.txt
│  │     ├─ 3.txt
│  │     ├─ 4.txt
│  │     ├─ 5.txt
│  │     ├─ 6.txt
│  │     ├─ 7.txt
│  │     ├─ 8.txt
│  │     └─ 9.txt
│  ├─ 세계
│  │  ├─ 1.txt
│  │  ├─ 10.txt
│  │  ├─ 11.txt
│  │  ├─ 12.txt
│  │  ├─ 13.txt
│  │  ├─ 14.txt
│  │  ├─ 15.txt
│  │  ├─ 16.txt
│  │  ├─ 17.txt
│  │  ├─ 18.txt
│  │  ├─ 19.txt
│  │  ├─ 2.txt
│  │  ├─ 20.txt
│  │  ├─ 21.txt
│  │  ├─ 22.txt
│  │  ├─ 23.txt
│  │  ├─ 24.txt
│  │  ├─ 25.txt
│  │  ├─ 3.txt
│  │  ├─ 4.txt
│  │  ├─ 5.txt
│  │  ├─ 6.txt
│  │  ├─ 7.txt
│  │  ├─ 8.txt
│  │  └─ 9.txt
│  └─ 정치
│     ├─ 1.txt
│     ├─ 10.txt
│     ├─ 11.txt
│     ├─ 12.txt
│     ├─ 13.txt
│     ├─ 14.txt
│     ├─ 15.txt
│     ├─ 16.txt
│     ├─ 17.txt
│     ├─ 18.txt
│     ├─ 19.txt
│     ├─ 2.txt
│     ├─ 20.txt
│     ├─ 21.txt
│     ├─ 22.txt
│     ├─ 23.txt
│     ├─ 24.txt
│     ├─ 25.txt
│     ├─ 3.txt
│     ├─ 4.txt
│     ├─ 5.txt
│     ├─ 6.txt
│     ├─ 7.txt
│     ├─ 8.txt
│     └─ 9.txt
├─ main.py
├─ README.md
└─ src
   ├─ credentials.txt
   ├─ function
   │  ├─ DATA
   │  ├─ newsSection.py
   │  ├─ papago.py
   │  ├─ textConfig.py
   │  ├─ var.py
   │  └─ __pycache__
   │     ├─ papago.cpython-311.pyc
   │     └─ var.cpython-311.pyc
   ├─ loginWindow.py
   ├─ NewsWindow.py
   ├─ test
   │  ├─ articleTest.json
   │  └─ test.py
   └─ __pycache__
      ├─ loginWindow.cpython-311.pyc
      ├─ newsSection.cpython-311.pyc
      ├─ NewsWindow.cpython-311.pyc
      ├─ papago.cpython-311.pyc
      └─ var.cpython-311.pyc

```