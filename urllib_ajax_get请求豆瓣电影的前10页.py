import  urllib.parse
import urllib.request
# url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
#（1）请求对象的定制
# request= urllib.request.Request(url = url,headers = headers)
# response = urllib.request.urlopen(request)
# content = response.read(response).encode('utf-8')
# print(content)
def create_response(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
    data = {
        'start' : (page-1) * 20,
        'limit' : 20
    }
    data = urllib.parse.urlencode(data)#不需要加encode，因为此处为get请求  只有post请求需要使用encode
    url = base_url + data
    request = urllib.request.Request(url = url, headers = headers)
    return request
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content,page):
    with open('douban_'+ str(page) + '.json','w',encoding= 'utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int (input('请输入起始页码：'))
    end_page = int (input('请输入结束的页码：'))
    for page in range(start_page, end_page + 1):
        request = create_response(page)
        content = get_content(request)
        down_load(content,page)