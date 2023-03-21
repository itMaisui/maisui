import urllib.request
url = 'http://zh-hans.ipshu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}

# hander build_opener   open
#请求对象的定制
request = urllib.request.Request(url= url,headers= headers)
proxies = {'http':'222.74.73.202:42055'}

hander = urllib.request.ProxyHandler(proxies= proxies)
opener = urllib.request.build_opener(hander)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(content)