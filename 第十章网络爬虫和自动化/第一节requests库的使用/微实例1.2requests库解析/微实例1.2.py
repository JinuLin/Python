# 微实例10.1.2requests库解析
import requests
"""
requests库中的网页请求函数：
get(url [,timeout=n]) 对应于HTTP的GET方式，获取网页最常用的方法，
可以增加timeout=n参数，设定每次请求超时时间为n秒
post(url, data = {'key':'value'}) 对应于HTTP的POST方式，其中字典用于传递客户数据
delete(url) 对应于HTTP的DELETE方式
head(url) 对应于HTTP的HEAD方式
options(url) 对应于HTTP的OPTIONS方式
put(url,data = {key':'value'}) 对应于HTTP的PUT方式，其中字典用于传递客户数据
"""
"""
get()是获取网页最常用的方式，在调用
requests.get()函数后，返回的网页内容会保存为一
个Response 对象，其中，get()函数的参数url 必须
链接采用HTTP 或HTTPS方式访问
"""
r = requests.get('https://www.baidu.com') # 使用git方法打开百度链接
print(type(r)) # 返回Reponse对象
"""
和浏览器的交互过程一样，requests.get()代表请求过程，
它返回的Response对象代表响应。
返回内容作为一个对象更便于操作，Response对象的属性如下所示，需要采用<a>.<b>形式使用。

status_code HTTP请求的返回状态，整数，200表示连接成功，404表示失败
text HTTP响应内容的字符串形式，即url对应的页面内容
encoding HTTP响应内容的编码方式
content HTTP响应内容的二进制形式
"""
"""
status_code属性返回请求HTTP后的状态，在处
理数据之前要先判断状态情况，如果请求未被响应，
需要终止内容处理。
text属性是请求的页面内容，以字符串形式展示。
encoding 属性非常重要，它给出了返回页面内容的
编码方式，可以通过对encoding属性赋值更改编码方式，
以便于处理中文字符。
content属性是页面内容的二进制形式
"""
print(r.status_code) # 返回状态
print(r.text) # 返回内容，观察中文是否能正常显示
print(r.encoding) # 默认编码是ISO-8859-1，所以中文是乱码
r.encoding = 'utf-8' # 更改编码为utf-8
print(r.text)
