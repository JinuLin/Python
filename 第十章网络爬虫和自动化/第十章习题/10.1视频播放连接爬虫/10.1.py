import requests
from bs4 import BeautifulSoup


def get_html(url):
    # 添加请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response.encoding = 'utf-8'
    return response.text


def find_links(text):
    # 指定解析器以避免警告
    soup = BeautifulSoup(text, features="html.parser")
    
    # 添加异常处理以避免 IndexError
    try:
        # 提取标题
        title_element = soup.find('title')
        if title_element:
            # 从<title>标签中提取剧名
            title = title_element.get_text().strip().split('-')[0]
        else:
            title = "未找到标题"
            
        # 提取评分
        score = "暂无评分"
        score_elements = soup.find_all('div')
        for element in score_elements:
            if '分' in element.get_text() and '简介' in element.get_text():
                text = element.get_text()
                import re
                score_match = re.search(r'(\d+\.\d+)分', text)
                if score_match:
                    score = score_match.group(1)
                break
            
        # 提取简介
        desc = "暂无简介"
        desc_elements = soup.find_all('div')
        for element in desc_elements:
            if '简介' in element.get_text() and len(element.get_text()) > 5:
                text = element.get_text()
                if '简介' in text and len(text) > 10:
                    # 简单处理提取简介文本
                    parts = text.split('简介')
                    if len(parts) > 1:
                        desc = parts[1].strip()[:50] + "..." if len(parts[1].strip()) > 50 else parts[1].strip()
                    break
        
        print('{} - {}分 - {}'.format(title, score, desc))
        
        # 提取剧集列表
        # 从页面内容看，剧集链接在包含"选集"文字的区域
        episode_area = soup.find_all('a', href=lambda x: x and 'video' in x if x else False)
        if episode_area:
            z = 0
            print('当前剧集：')
            # 限制显示前50集
            for link in episode_area[:50]:
                text = link.get_text().strip()
                if text and text != '查看全部':
                    print('{:^5}'.format(text), end='')
                    z = z + 1
                    if z % 10 == 0:
                        print('\n')
            if z % 10 != 0:
                print('\n')
        else:
            print("未找到剧集列表")
                
    except Exception as n:
        print(f"解析过程中出现错误: {n}")


# 添加异常处理
try:
    Text = get_html('https://www.soku.com/detail/show/XNjA4NTI=?spm=a2h0k.8191414.0.0')
    find_links(Text)
except requests.RequestException as e:
    print(f"网络请求失败: {e}")
except Exception as e:
    print(f"程序执行出错: {e}")