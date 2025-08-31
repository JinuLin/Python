# 微实例10.1.3获取一个HTML通用代码
"""
json()方法能够在HTTP响应内容中解析存在的JSON数据，这将带来解析HTTP的便利。
raise_for_status()方法能在非成功响应后产生异常，
即只要返回的请求状态status_code不是200，
这个方法会产生一个异常，用于try…except语句。
使用异常处理语句可以避免设置一堆复杂的if语句，
只需要在收到响应调用这个方法，就可以避开状态字200以外的各种意外情况。
"""
import requests


def get_html_text(u):
    try:
        r = requests.get(u, timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发异常
        r.encoding = 'utf-8'  # 无论原来用什么编码，都改成utf-8
        return r.text
    except requests.RequestException:
        return ""


url = "https://www.baidu.com"
print(get_html_text(url))
"""
HTTP 协议定义了客户端与服务器交互的不同方法，最基本的方法是GET和POST。
顾名思义，GET可以根据某链接获得内容，
POST用于发送内容。
然而，GET也可以向链接提交内容
1.GET 方式可以通过URL提交数据，待提交数据是URL 的一部分；
采用POST方式，待提交数据放置在HTML HEADER内；
2.GET方式提交的数据最多不超过1024字节，POST没有对提交内容的长度限制。
3.安全性问题。如1所述，使用GET时参数会显示在URL中，而POST不会。
所以，如果这些数据是非敏感数据，那么使用GET；
如果提交数据是敏感数据，建议采用POST方式。
"""
