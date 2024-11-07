# 微实例6.6.2带排除的Hamlet英文词频统计
"""
之前程序，高频单词大多数是冠词、代词、连接词等语法型词汇，并不能代表文章的含义。
进一步，可以采用集合类型构建一个排除词汇库excludes，在输出结果中排除这个词汇库中内容
"""
excludes = {"the", "and", "of", "you", "a", "i", "my", "in"}


def gettext():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
    return txt


hamletTxt = gettext()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del (counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
"""
排除后依旧有许多语法型词汇，如果希望排除更多，可以继续增加excludes的内容
"""
