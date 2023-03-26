from selenium import webdriver
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

input = browser.find_element_by_id('su')
#获取属性
# print(input.get_attribute('class'))

#获取标签名
# print(input.tag_name)

#获取元素文本
print(input.text)

#








