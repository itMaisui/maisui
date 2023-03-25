from bs4 import BeautifulSoup

#通过解析本地文件 来将bs4的基础语法进行讲解

#加载本地文件  默认打开文件的编码格式是gbk  所以在打开的时候要指定编码
# soup = BeautifulSoup(open('bs4的基本使用.html', encoding='utf-8'),'lxml')
# print(soup)


#根据标签的名字来查找节点
#例如  查找标签为a的节点
#  此处查找到的是第一个标签为a的节点
# soup = BeautifulSoup(open('bs4的基本使用.html', encoding='utf-8'),'lxml')
#print(soup.a)

#查找到的是第一个标签为a的属性和属性值
# soup = BeautifulSoup(open('bs4的基本使用.html', encoding='utf-8'),'lxml')
# print(soup.a.attrs)

#bs4 的一些函数
# 1）   find
# soup = BeautifulSoup(open('bs4的基本使用.html', encoding='utf-8'),'lxml')
#返回的是第一个符合条件的数据
#print(soup.find('a'))

#根据属性的值来找到对应的标签对象
# print(soup.find('a', id='222'))

#如果想查找属性为class的值 不可以直接查找class  因为class已经被定义  如果想查找class，可以将class改成class_
# print(soup.find('a', class_="a1"))


# 2)   find_all
soup = BeautifulSoup(open('bs4的基本使用.html', encoding='utf-8'),'lxml')

#find_all可查看到所有标签 并返回一个列表  并返回所有为a的标签
# print(soup.find_all('a'))

#查找所有a标签和span标签，注意 需要在find_all的参数中添加的是列表的数据
# print(soup.find_all(['a', 'span']))

#查找前两个标签为li的数据
# print(soup.find_all('li', limit=2))


# 3)    select

# select 方法返回的数一个列表  并且会返回多个数据
# print(soup.select('a'))

# 可以用.代表class  我们把这种操作叫做类选择器
# print(soup.select('.a1'))

# id  #可以代表id  例如  #l1可以查找id为l1的标签
# print(soup.select('#l1'))

#属性选择器   通过属性来寻找对应的标签
# 查找到li标签中有id的标签
# print(soup.select('li[id]'))

#层级选择器      空格  大于号  逗号

# 找div下面的li   后代选择器  可以利用 空格
# print(soup.select('div li'))

#子代选择器  查找某标签的第一级子标签
#注意  很多计算机编程语言中，如果不加空格不会输出内容，在bs4中不会报错，会显示内容
# print(soup.select('div > ul > li'))

#找到a标签和li标签的所有对象
# print(soup.select('a,li'))



#节点信息
#1 获取节点内容
# 如果标签对象中，除了内容还有标签  那么string就获取不到数据  而get_text()可以获取数据  所以推荐使用后者
# obj = soup.select('#d1')[0]  # 返回的是一个列表的值
# print(obj)
# print(obj.get_text())

#2节点的属性
# 通过id来获取p标签
obj = soup.select('#p1')[0]

#name 返回的是标签的名字
# print(obj.name)

# attrs  将属性值作为一个字典返回
# print(obj.attrs)

# 获取节点的属性
obj = soup.select('#p1')[0]
#方式1  print(obj.attrs.get('class'))
#方式2  print(obj.get('class'))
#方式3  print(obj['class'])






