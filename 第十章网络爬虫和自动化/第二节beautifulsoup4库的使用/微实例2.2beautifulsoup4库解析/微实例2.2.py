# 微实例10.2.2beautifulsoup4库解析
"""
beautifulsoup4库中最主要的是BeautifulSoup类，
每个实例化的对象相当于一个页面。采用from…import导入库中类后，
使用BeautifulSoup()创建一个BeautifulSoup对象。
"""
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.baidu.com')
r.encoding = 'utf-8' # 为了简化代码，没有考虑异常情况
soup = BeautifulSoup(r.text,features="html.parser") # soup就是一个BeautifulSoup对象
print(type(soup))
"""
创建的BeautifulSoup对象是一个树形结构，
它包含HTML页面里的每一个Tag（标签）元素，如<head>、<body>等。
具体来说，HTML中的主要结构都变成了BeautifulSoup对象的一个属性，
可以直接用<a>.<b>形式获得，其中<b>的名字采用HTML中标签的名字。
"""
"""
BeautifulSoup对象常用属性：
head HTML页面的<head>内容
title HTML页面标题，在<head>之中，由<title>标记
body HTML页面的<body>内容
p HTML页面中第一个<p>内容
strings HTML页面所有呈现在Web上的字符串，即标签的内容
stripped_strings HTML页面所有呈现在Web上的非空格字符串
"""
print(soup.head)
title = soup.title
print(title)
print(type(title))
print(soup.p)

"""
每一个Tag标签在beautifulsoup4库中也是一个对象，称为Tag对象。
上例中，title是一个标签对象。每个标签对象在HTML中都有类似的结构：
<a class="mnav" href="https://www.baidu.com">百度</a>
（百度是：<a class="mnav c-font-normal c-color-t" href="//news.baidu.com/" target="_blank">新闻</a>）
其中，尖括号（<>）中的标签的名字是name，尖括号内其他项是attrs，尖括号之间的内容是string。
因此，可以通过Tag对象的name、attrs和string属性获得相应内容，采用<a>.<b>的语法形式。
"""
"""
标签对象的常用属性
name 字符串，标签的名字，比如div
attrs 字典，包含了原来页面Tag所有的属性，比如href
contents 列表，这个Tag下所有子Tag的内容
string 字符串，Tag所包围的文本，网页中真实的文字
"""
print(soup.a)
print(soup.a.name)
print(soup.a.attrs)
print(soup.a.string)
print(title.name)
print(title.string)
print(soup.p.contents)
"""
由于HTML语法可以在标签中嵌套其他标签，
所以，string属性的返回值遵循如下原则：
1.如果标签内部没有其他标签，string属性返回其中的内容；
2.如果标签内部有其他标签，但只有一个标签，string属性返回最里面标签的内容；
3.如果标签内部有超过1层嵌套的标签，string属性返回None（空字符串）。
HTML语法中同一个标签会有很多内容，例如<a>标签，百度有28个，直接调用soup.a只能返回第一个。
当需要列出标签对应的所有内容或者需要找到非第一个标签时，
需要用到BeautifulSoup的find()和find_all()方法。
这两个方法会遍历整个HTML文档，按照条件返回标签内容。
BeautifulSoup.find_all(name,attrs,recursive,string,limit)
作用：根据参数找到对应标签，返回列表类型。
"""
a = soup.find_all('a') # 返回所有a标签
print(len(a))
print(soup.find_all('script'))
print(soup.find_all(src=True)) # 返回所有src属性的标签
import re # 使用正则表达式库，可以实现字符串片段匹配
print(soup.find_all('srcipt',{'src':re.compile('flexible')}))
print(soup.find_all(string=re.compile('百度')))
"""
简单说，BeautifulSoup的find_all()方法可以根据标签名字、标签属性和内容检索并返回标签列表，
通过片段字符串检索时需要使用正则表达式re函数库，
re是Python标准库，直接通过import re即可使用。
采用re.compile('flexible')实现对片段字符串（如'flexible'）的检索。
当对标签属性检索时，属性和对应的值采用JSON格式，例如：
'src':re.compile('flexible')
其中，键值对中值的部分可以是字符串或者正则表达式。
"""
"""
正则表达式是表达和操作字符串的一种逻辑表达，一般在计算机编译器中使用。
Python语言采用正则表达式辅助字符串查找。
正则表达式是一种规则，只要字符串符合这个规则，就算作匹配。
例如，通过re.compile()函数注册一个正则表达式'flexible'，则所有包含表达式的字符串都与它匹配。
除了字符串，正则表达式还可以通过*+{}等符号扩展功能。
"""
"""
除了find_all()方法，BeautifulSoup类还提供一个find()方法，
它们的区别只是前者返回全部结果而后者返回找到的第一个结果，
find_all()函数由于可能返回更多结果，所以采用列表形式；find()函数返回字符串形式。
"""
