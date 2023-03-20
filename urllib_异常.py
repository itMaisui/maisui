import urllib.request
import urllib.error
try:
    url = 'https://blog.csdn.net/leyi520/article/details/128385929?spm=1000.2115.3001.6382'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
    request = urllib.request.Request(url = url,headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.URLError:
    print("url错误")
except urllib.error.HTTPError:
    print("http错误")