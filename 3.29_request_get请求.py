


#urllib
# 一个类型六个方法
#1   get请求
#2    post请求
#3    ajax的get请求
#4    ajax的post请求
#5    cookie登入
#6    代理


#request
#    一个类型六个属性
#1   get请求
#2    post请求
#3    代理
#4    cookie  验证码




import requests
url = 'https://www.baidu.com/s?'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'}
data = {'wd' : '南昌'}
response = requests.get(url=url, params=data, headers=headers)
context = response.text
print(context)

#1  参数使用params传递
#2  参数无需urlencode编码
#3  不需要请求对象的定制
#4   请求资源路径的问号可以加也可以不加
