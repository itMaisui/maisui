import requests
url = 'https://www.baidu.com'
response = requests.get(url=url)
#  一个类型和六个属性
#为response类型
# print(type(response))

#以字符串的形式返回网页的原码  所以可以设置属性
# response.encoding = 'utf-8'
# print(response.text)

#返回一个url地址
# print(response.url)

#返回一个二进制的数据
# print(response.content)

#返回响应的状态码
# print(response.status_code)

#返回的是响应头
# print(response.headers)