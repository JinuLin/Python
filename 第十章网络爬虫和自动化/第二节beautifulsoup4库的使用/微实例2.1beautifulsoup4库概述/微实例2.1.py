# 微实例10.2.1beautifulsoup4库概述
"""
使用requests库获取HTML页面并将其转换成字符串后，
需要进一步解析HTML页面格式，提取有用信息，这需要处理HTML和XML的函数库。
beautifulsoup4库，也称为Beautiful Soup库或bs4库，用于解析和处理HTML和XML。
需要注意，它不是BeautifulSoup库。
它的最大优点是能根据HTML和XML语法建立解析树，进而高效解析其中的内容。
HTML建立的Web页面一般非常复杂，除了有用的内容信息外，
还包括大量用于页面格式的元素，直接解析一个Web网页需要深入了解HTML语法，而且比较复杂。
beautifulsoup4库将专业的Web页面格式解析部分封装成函数，
提供了若干有用且便捷的处理函数。
"""
""""
beautifulsoup4库采用面向对象思想实现，简单说，它把每个页面当做一个对象，
通过<a>.<b>的方式调用对象的属性（即包含的内容），
或者通过<a>.<b>()的方式调用方法（即处理函数）。
"""
"""
在使用beautifulsoup4库之前，需要进行引用，
由于这个库的名字非常特殊且采用面向对象方式组织，
可以用 from…import方式从库中直接引用BeautifulSoup类，方法如下。
"""
from bs4 import BeautifulSoup

html_doc = "<html><head><title>测试页面</title></head><body><p>这是一个测试段落。</p></body></html>"
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title.string)
