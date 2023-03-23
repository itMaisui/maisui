import urllib.request
from lxml import etree
#需求 下载前10页的照片
# 第一页https://sc.chinaz.com/tupian/xingganmeinvtupian.html
# 第二页https://sc.chinaz.com/tupian/xingganmeinvtupian_2.html

#1 请求对象的定制
def creat_request(page):
    if(page ==1):
        url = 'https://sc.chinaz.com/tupian/xingganmeinvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/xingganmeinvtupian_' + str(page) + '.html'
    herders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
    request = urllib.request.Request(url=url, headers=herders)
    return request

#2 获取网页源码
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
#3 下载
def down_load(content):
    #3（1）下载图片
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="container"]//div//@alt')
    # 一般设计图片的网站都会进行懒加载  此处没有//div[@class="container"]//div/img//@src
    src_list = tree.xpath('//div[@class="container"]//div/img//@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        print(name,url)
        # urllib.request.urlretrieve('图片地址'，’文件的名字‘)
        urllib.request.urlretrieve(url=url, filename='./beauty/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        request = creat_request(page)
        content = get_content(request)
        down_load(content)



