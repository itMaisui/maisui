import urllib.request
headers = {#':authority':'dianying.taobao.com',
#':method':'GET',
#':path':'/cityAction.json?activityId&_ksTS=1679651192236_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
#':scheme':'https',
'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
#'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'bx-v':'2.2.3',
'cookie':'t=12bf678345a388617936fe0cfa205ebd; cookie2=1767b09e6dc0a0a8c21842f41805f681; v=0; _tb_token_=e6339ede35318; cna=FXOQHMruo3ICAbfZHH3c64m7; xlly_s=1; tfstk=cjiRB-_31IAoqbd30uLcT7qdoEJcagv3GwPCvc00UGWJNesdAsASjcU__py3_7pA.; l=fBSl6Ke4NPc31DaFBO5Bhurza77OXQAb4SFzaNbMiIEGa6tNtF_DjNCsdkLWSdtjgTCbDetzMXYONdLHR3x0lc0c0KDtBaVsExvtaQtJe; isg=BPHxr5SGMZ0Oep2JMo0NMq-2AH2L3mVQMh3eFtMEbbjX-hFMGy7SINscHI6cav2I',
'referer':'https://dianying.taobao.com/index.htm?n_s=new',
'sec-ch-ua':'"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
'x-requested-with':'XMLHttpRequest',
}

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1679651192236_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
#split 切割
content = content.split('(')[1].split(')')[0]

with open('淘票票.json', 'w',encoding='utf-8') as fp:
    fp.write(content)
import json
import jsonpath
obj = json.load(open('淘票票.json'))
city_list = jsonpath.jsonpath(obj,'$..regionName')
print(city_list)