#想要跳过登入页面 爬取主页面的数据
#个人页面一般是utf-8 而登入页面一般为gb2312
import urllib.request
url = 'https://weibo.com/ajax/profile/info?uid=5767282158'
headers = {#':authority':'weibo.com',
#':method':'GET',
#':path':'/ajax/profile/info?uid=5767282158',
#':scheme':'https',
'accept':'application/json, text/plain, */*',
#'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'client-version':'v2.40.7',##cookie中携带着登入信息，如果有登入之后的cookie，那么我们就可以携带着cookie进入到任何页面
'cookie':'XSRF-TOKEN=xvGMWigKlQ8WW4Qoptj9_y5l; PC_TOKEN=63573f391f; login_sid_t=b00ddea5688f01e31c6bcfcb6011a2db; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=weibo.com; Apache=6221379249498.096.1679304831458; SINAGLOBAL=6221379249498.096.1679304831458; ULV=1679304831461:1:1:1:6221379249498.096.1679304831458:; wb_view_log=1707*10671.5; WBtopGlobal_register_version=2023032017; SSOLoginState=1679304873; UPSTREAM-V-WEIBO-COM=b09171a17b2b5a470c42e2f713edace0; webim_unReadCount=%7B%22time%22%3A1679304906091%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A1%2C%22msgbox%22%3A0%7D; SCF=AuoRBd7yfdb1nLQLc5S5g2wC3KYjALP6z30PQTXmxFeKAvTrZf5-EBrV_BtscFdN-KHY_O6MHJ7BNYFrLPgCFno.; SUB=_2A25JHFiqDeRhGeNJ7VUT-CzNzjSIHXVqaM1irDV8PUNbmtAGLWKlkW9NS7tOUSIr3rqyaoBqlYvChS5Kvz5rHC7B; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5S_V2QcJw9_cP6WcIqqkWJ5JpX5KMhUgL.Fo-NSoME1hzpSKn2dJLoIEQLxK.L1h5L1hqLxK-L1h-L1h._TCX_TCXLxK-LBK-L1KBLxKnLBoML1K2t; ALF=1681896954; WBPSESS=Hd2Nej4fQvvW-a-ehiumLQRkaoFd5nf_LCcepje0LR4LaKg0nAOriCed2batbbjsHvuqqh7rRy1I92CBnawxK_ALu3zo4l5HC5dTkrmx-HzXmigtA7Q4CsdQFFzz5AkulC_jlOCibv0E9Wy8dFRZxQ==',
'referer':'https://weibo.com/u/5767282158',#referer  判断当前路径是不是由上一个路径进来的  一般情况下  做图片防盗链
'sec-ch-ua':'"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'server-version':'v2023.03.17.1',
'traceparent':'00-e04c9a22063d4a72c1b734cd0d6ca24a-643e85227f0064a1-00',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
'x-requested-with':'XMLHttpRequest',
'x-xsrf-token':'xvGMWigKlQ8WW4Qoptj9_y5l',
}
request =urllib.request.Request(url = url,headers= headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)