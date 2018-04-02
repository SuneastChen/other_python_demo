import requests
import random
from PIL import Image 
import ssl
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
from urllib.parse import urlencode
from http.cookiejar import CookieJar
import easygui
import re

def b_opener():
    # 第一步:构建opener(浏览器)
    cookie = CookieJar()  # 创建cookie对象,用来保存cookie的值
    cookie_handler = HTTPCookieProcessor(cookie) # 构建一个cookie_handler
    opener = build_opener(cookie_handler)  # 创建一个自定义的opener
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0')] 
    return opener



def open_url(opener,url,data=None):

    # 第二步:构建登陆的req(即浏览器要打开的对象)
    if data:
        # data = {'email':'15161580934','password':'renren789.'}
        data = urlencode(data).encode('utf-8')
        req = Request(url,data=data)
    else:
        req = Request(url)

    # 第三步:用opener打开req对象,post登陆,保存了登陆的cookie
    ssl._create_default_https_context = ssl._create_unverified_context
    response = opener.open(req) 
    return response.read()

def log_in(username,password):
    capt_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&%d' % random.random()
    
    with open('capt.jpg','wb') as f:
        f.write(open_url(opener,capt_url))
    Image.open('capt.jpg').show()
    capt = easygui.enterbox(msg='请输入验证码数字位置,用空格隔开(如"2 5 8"):',title='输入验证码:',default=None,strip=True,image=None)   #单个输入框
    yzm = ''
    for num in capt.split(' '):
        num = int(num)
        x_num = (num-1) % 4
        x = 35 + (x_num)*73
        y_num = int((num-1) / 4)
        y = 40 + (y_num)*80
        yzm += str(x) + ',' + str(y) + ','
    yzm = yzm.strip(',')
    # print(yzm)
    
    yzm_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
    data = {'answer': yzm,
            'login_site': 'E',
            'rand': 'sjrand'}
    yzm_res = open_url(opener, yzm_url, data=data).decode('utf-8')
    print(yzm_res)

    log_url = 'https://kyfw.12306.cn/passport/web/login'
    data = {'username': username,
            'password': password,
            'appid': 'otn'}
    log_res = open_url(opener, log_url, data=data)
    print(log_res.decode('utf-8'))


def get_stations():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9031'
    res_stations = open_url(opener, url).decode('utf-8')
    # print(res_stations)
    start = easygui.enterbox(msg='请输入出发站:',title='输入出发站:',default=None,strip=True,image=None)   #单个输入框
    start_stion = re.search(start+r'[|](.+?)[|]',res_stations).group(1)
    print(start_stion)
    end = easygui.enterbox(msg='请输入终点站:',title='输入终点站:',default=None,strip=True,image=None)   #单个输入框
    end_stion = re.search(end+r'[|](.+?)[|]',res_stations).group(1)
    print(end_stion)
    train_date = easygui.enterbox(msg='请输入乘车日期(格式:2018-01-01):',title='输入乘车日期:',default='2017-',strip=True,image=None)
    return start_stion,end_stion,train_date



if __name__ == '__main__':
    opener = b_opener()
    log_in(username='langcheng', password='teilu789')
    # get_stations()



'''
0 乱入码
1 预订
2 930000Z18003
3 Z180          # 车次
4 WAR           
5 BJP
6 WMR
7 BJP
8 18:46        # 出发时间
9 09:40        # 到达时间
10 38:54       # 历时
11 Y
12 XrpGTxMMXe3ne5h1%2B4o

%2FaiYhA0IeGhwjQEm8pRQp6VlG7%2FOjJmikmGwB39o%3D
13 20171130    # 出发日期
14 3
15 R1
16 02
17 22
18 0
19 0
20 
21         # 高级软卧
22          # 其他
23 17       # 软卧
24 
25 
26 无       # 无座
27 
28 有       # 硬卧
29 有       # 硬座
30          # 二等座
31          # 一等座
32          # 特等座
33          # 动卧
34 10401030
35 1413
'''

