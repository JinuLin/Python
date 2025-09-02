import urllib.robotparser

import bs4
import requests


def back_html(u):
    html_back = requests.get(u)
    soup = bs4.BeautifulSoup(html_back.text, 'html.parser')
    print('网页代码如下：')
    print(soup.prettify())


def robot_ana(u, url_want, str_in):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(u)
    rp.read()
    if rp.can_fetch("*", url_want):
        print('robots 协议未禁止')
        back_html('https://' + url_want)
    else:
        print("十分抱歉，对方网页禁止了您的访问；请看以下规则")
        print(str_in)


url = input("请输入您要爬取的网页,不用输http：")
real_url = url.split('/', 1)[0]
robot_url = 'https://' + real_url + '/robots.txt'
robot_read = requests.get(robot_url)
robot_read.encoding = robot_read.apparent_encoding
if robot_read.status_code != 200:
    print('您爬取的网站没有设置 robots 规则，正在返回网页源代码')
    back_html('https://' + url)
else:
    print("正在分析规则..")
    robot_ana(robot_url, url, robot_read.text)
