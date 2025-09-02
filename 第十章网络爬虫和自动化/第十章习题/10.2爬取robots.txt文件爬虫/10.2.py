import requests


def get_robot_txt(u):
    response = requests.get(u)
    response.raise_for_status()
    return response.text


def analyse_txt(u, t):
    try:
        file = open('ban.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
        file = open('ban.txt', 'w', encoding='utf-8')
    s = t.split('User-agent:')
    for i in range(1, len(s)):
        sub = s[i].split('\r\n')
        string = '对于爬虫代理: {} ,以下网址不能访问：'.format(sub[0])
        print(string)
        file.write(string + '\r\n')
        for j in range(1, len(sub)):
            if sub[j][:9] == 'Disallow:':
                string = u + sub[j][10:]
                print(string)
                file.write(string + '\r\n')
    file.close()

url = 'https://www.baidu.com'
robots = '/robots.txt'
text = get_robot_txt(url + robots)
analyse_txt(url, text)
