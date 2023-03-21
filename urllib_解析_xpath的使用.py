from lxml import etree

#xpath解析
#1 解析本地文件
# 使用的是etree.parse
#2服务器响应的数据 response.read().decode('utf-8')
# 使用的是etree.HTML()

#运用xpath解析本地文件
# tree = etree.parse('urllib_解析_xpath的使用.html')
# print(tree)

# xpath 的基本语法

#tree。xpath('xpath路径')
# 1.  //查找所有子孙结点，不考虑层级关系
#     /找直接子节点

# 例如 查找ul下面的li
#li_list = tree.xpath('//body//li')  //查找的是所有子孙结点，不考虑层级关系

# 2谓语查询
#   //div[@id]
#   //div[@id="maincontent"]

# 例如  查找所有有id属性的标签
#text()获取标签中的内容
#li_list = tree.xpath('//ul/li[@id]')

#例如  查找id为12的标签  注意引号的问题 单引号里面使用双引号
#li_list = tree.xpath.('//ul/li/[@id="1"]')

#3属性查询
#   //@class

#查找id为11的li标签的class的属性值
#li = tree.xpath('//ul/li[id="11"]/@class')

#4 模糊查询
#   //div[contains(@id,"he")]
#   //div[starts-with(@id,"he")]    starts with 以什么为开头

#例如  查询id中含有c的li标签
# li = tree.xpath('//ul/li[contains(@id,"c")]')

#查询id中包含c开头的li标签
# li_List = tree.xpath('//ul/li[starts-with(id,"c")]')

#5 内容查询
#   //div/h1/text()

#6 逻辑运算
#   //div[@id="head" and @class="s_down"]
#   //title | //price

# 查询id为11 class为c1的li标签
# li_list = tree.xpath('//ul/li[@id="11" and @class="c1"]')

#错误写法  li_list = tree.xpath('//ul/li[@id="11" | @class="c1"]/text()')

#正确写法  li_list = tree.xpath('//ul/li[@id="11"]/text() | ur/li/[@id= "12"]/text()')
