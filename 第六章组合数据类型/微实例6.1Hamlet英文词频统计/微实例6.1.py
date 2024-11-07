# 微实例6.6.1Hamlet英文词频统计
"""
下载对应文本，Hamlet.txt，进行统计。
统计词频的第二步是对每个单词进行计数。假设将单词保存在变量word中，使用一个字典类型counts={}，统计单词出现的次数可采用如下代码:counts[word]=counts[word]+1
当遇到一个新词时，单词没有出现在字典结构中，则需要在字典中新建键值对counts[new word]=1
因此,无论词是否在字典中,加入字典counts中的处理逻辑可以统一表示如下
if word in counts:
"""

"""
统计 Hamlet英文词频的第一步是分解并提取英文文章的单词。

"""


def gettext():
    txt = open("hamlet.txt", "r").read()
    # 同一个单词会存在大小写不同形式，但计数却不能区分大小写。
    txt = txt.lower()
    # 假设Hamlet文本由变量txt表示，可以通过 txt.lower()函数将字母变成小写，
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        # 排除原文大小写差异对词频统计的干扰英文单词的分隔可以是空格、标点符号或者特殊符号。
        txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
        # 为统一分隔方式，可以将各名种特殊字符和标点符号使用txt.replace()方法替换成空格，再提取单词。
    return txt


"""
统计词频的第二步是对每个单词进行计数。
"""
hamletTxt = gettext()
words = hamletTxt.split()
counts = {}  # 假设将单词保存在word变量中，使用一个字典类型：counts = {}
# 统计单词出现的次数：counts[word] = counts[word]+ 1
for word in words:
    """
当遇到一个新词时，单词没有出现在字典结构中，则需要在字典中新建键值对：counts[new_word]=1
无论词是否在字典中,加入字典counts中的处理逻辑可以统一表示如下：
if word in counts:
    counts[word]=counts[word]+1
else:
    counts[word]=1
或者，这个处理逻辑可以更简洁地表示为如下代码:
counts[word]=counts.get(word,0)+1
    """
    counts[word] = counts.get(word, 0) + 1
    # 字典类型的 counts.get(word,0)方法表示：如果word在counts 中，则返回对应的word值，
    # 如果word不在counts中，则返回 0。

"""
该实例的第三步是对单词的统计值从高到低进行排序，输出前10个高频通，并格式化打印输出。
"""
"""
由于字典类型没有顺序，
需要将其转换为有顺序的列表类再使用sort()方法和lambda函数配合实现根据单词出现的次数对元素进行排序。
最后输出排序结果前10位的单词。
"""
items = list(counts.items())  # 将字典转换为记录列表
items.sort(key=lambda x: x[1], reverse=True)
# 以记录第2列排序
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
