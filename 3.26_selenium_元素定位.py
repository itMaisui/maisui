from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.baidu.com'
browser.get(url)
#元素定位:自动化要做的就是模拟鼠标和键盘来操作这些元素，点击，输入等等，操作这些元素前首先要找到他们，webDriver提供很对的定位元素的方法

#根据id来查找对象
#方法1 button = browser.find_element_by_id('su')
#####   方法2  button = browser.find_element('id','su')  建议使用方法2

#根据标签的属性的属性值来获取对象的
# button = browser.find_element_by_name('wd')

#根据xpath语句来获取对象  element后面加s返回列表
# button = browser.find_elements_by_xpath('//input[@id="su"]')
# button = browser.find_element(by='xpath',value='//imput[@id="su"]')

#tag_name  标签的名字   根据标签的名字来获取对象
# button = browser.find_element_by_tag_name('ipunt')

#  使用的是bs4的语法来实现的
# button = browser.find_element_by_css_selector('#su')

#过去当前页面超链接
button = browser.find_element_by_link_text('地图')
print(button)