import requests
import json
url = 'https://fanyi.baidu.com/sug'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'}
data = {'kw': 'big'}
response = requests.post(url=url, data=data, headers=headers)
content = response.text
obj = json.loads(content)
print(obj)

#post请求不需要编解码
#post的请求的参数为data
#不需要请求对象的定制








