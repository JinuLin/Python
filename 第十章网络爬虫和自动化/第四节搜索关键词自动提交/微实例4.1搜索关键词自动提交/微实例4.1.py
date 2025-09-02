# 微实例10.4.1搜索关键词自动提交
import json
import re

import requests
from bs4 import BeautifulSoup


def get_keyword_result(keyword):
    url = 'https://www.baidu.com/s?wd=' + keyword
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return ""


def parser_links(html):
    if not html:
        print("HTML内容为空")
        return []

    soup = BeautifulSoup(html, "html.parser")
    links = []

    # 方法1: 查找包含data-tools属性的div元素
    for div in soup.find_all('div', {'data-tools': re.compile('title')}):
        try:
            data = div.attrs['data-tools']
            d = json.loads(data)
            links.append(d['title'])
        except (KeyError, json.JSONDecodeError) :
            continue

    # 方法2: 查找h3标签中的标题（百度搜索结果常用格式）
    if not links:
        for h3 in soup.find_all('h3'):
            a_tag = h3.find('a')
            if a_tag and a_tag.get_text():
                title = a_tag.get_text().strip()
                if title not in links:
                    links.append(title)

    # 方法3: 查找所有包含特定class的搜索结果标题
    if not links:
        for div in soup.find_all('div', class_=re.compile('result|c-container')):
            h3_tag = div.find('h3')
            if h3_tag:
                a_tag = h3_tag.find('a')
                if a_tag and a_tag.get_text():
                    title = a_tag.get_text().strip()
                    if title not in links:
                        links.append(title)

    return links


def main():
    html = get_keyword_result('Python')
    ls = parser_links(html)
    count = 1
    for i in ls:
        print("[{:^3}]{}".format(count, i))
        count += 1


main()
