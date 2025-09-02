# 微实例10.3.1中国大学排名爬虫
"""
大学排名爬虫的构建需要三个重要步骤：
第一，从网络上获取网页内容；
第二，分析网页内容并提取有用数据到恰当的数据结构中；
第三，利用数据结构展示或进一步处理数据。
由于大学排名是一个典型的二维数据，因此，采用二维列表存储该排名所涉及的表单数据。
"""
"""
具体来说，采用requests 库爬取网页内容，使用beautifulsoup4库分析网页中数据，
提取310 个学校的排名及相关数据，存储到二维列表中，最后采用用户偏好的方式打印出来。
"""
import requests
from bs4 import BeautifulSoup

allUniv = []

"""
每个大学排名的数据信息被封装在一个<tr></tr>之间的结构中。
这是HTML语言表示表格中一行的标签，在这行中，每列内容采用<td></td>表示。
"""


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except (requests.RequestException, ValueError):
        return ""


"""
这个代码中每个td标签包含大学排名表格的一个列数值，与表头一一对应。
因此，如果要获得其中的数据，需要首先找到<tr></tr>标签，
并遍历其中每个<td></td>标签，获取其值写入程序的数据结构中
"""


def fill_univ_list(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        single_univ = []
        for td in ltd:
            # 使用 get_text() 提取所有文本，并去除多余空白
            text = td.get_text(strip=True)
            single_univ.append(text)
        allUniv.append(single_univ)


def print_univ_list(num):
    # 打印表头
    tilt = "{0:^4}\t{1:{5}^12}\t{2:^6}\t{3:^6}\t{4:^8}\t{6:^6}"
    print(tilt.format("排名", "学校名称", "省市", "类型", "总分", chr(12288), "办学层次"))

    for i in range(num):
        u = allUniv[i]
        # 处理学校名称，只保留中文名称部分
        school_info = u[1].strip()

        # 提取中文校名（去掉英文和标签）
        chinese_name = school_info
        # 查找英文名称开始位置
        english_start = -1
        for j, char in enumerate(school_info):
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
                english_start = j
                break

        if english_start != -1:
            chinese_name = school_info[:english_start].strip()

        # 再次检查并去除标签
        tags_start = -1
        for tag in ["双一流", "985", "211"]:
            pos = chinese_name.find(tag)
            if pos != -1:
                tags_start = pos if tags_start == -1 else min(tags_start, pos)

        if tags_start != -1:
            chinese_name = chinese_name[:tags_start].strip()

        # 格式化输出
        print(tilt.format(u[0], chinese_name, u[2], u[3], u[4], chr(12288), u[5]))


def main(num):
    url = 'https://www.shanghairanking.cn/rankings/bcur/2025'
    html = get_html_text(url)
    soup = BeautifulSoup(html, "html.parser")
    fill_univ_list(soup)
    print_univ_list(num)


main(10)
