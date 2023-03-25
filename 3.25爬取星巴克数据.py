import urllib.request

url = 'https://www.starbucks.com.cn/menu/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51'}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

name_list = soup.select('ul[class="grid padded-3 product"] strong')

print(name_list)

for name in name_list:
    print(name.get_text())













