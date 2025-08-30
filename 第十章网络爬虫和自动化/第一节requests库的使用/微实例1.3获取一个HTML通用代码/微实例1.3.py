# 微实例1.3获取一个HTML通用代码
import requests
def get_html_text(u):
    try:
        r = requests.get(u, timeout=30)
        r.raise_for_status() #如果状态不是200，引发异常
        r.encoding = 'utf-8' #无论原来用什么编码，都改成utf-8
        return r.text
    except requests.RequestException:
        return ""
url = "https://www.baidu.com"
print(get_html_text(url))