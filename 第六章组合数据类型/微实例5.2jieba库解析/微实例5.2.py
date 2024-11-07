# 微实例6.5.2jieba库解析
import jieba

"""
jieba库常用的分词函数：
jieba.cut(s)：精确模式，返回一个可迭代的数据类型
jieba.cut(s, cut_all=True)：全模式，输出文本s中所有可能单词
jieba.cut_for_search(s)：搜索引擎模式，适合搜索引擎建立索引的分词结果
jieba.lcut(s)：精确模式，返回一个列表类型，建议使用
jieba.lcut(s, cut_all=True)：全模式，返回一个列表类型，建议使用
jieba.lcut_for_search(s)：搜索引擎模式，返回一个列表类型，建议使用
jieba.add_word(w)：向分词词典中增加新词w
"""
print(jieba.lcut("中华人民共和国是一个伟大的国家"))
# jieba.lcut()返回精确模式，输出的分词能够完整且不多余地组成原始文本。
print(jieba.lcut("中华人民共和国是一个伟大的国家", cut_all=True))
# jieba.lcut(,True)函数返回全模式，输出原始文本中可能产生的所有问题，冗余性最大。
print(jieba.lcut_for_search("中华人民共和国是一个伟大的国家"))
# jieba.lcut_for_search函数返回搜索引擎模式，首先执行精确模式，然后再对其中的长词进一步切分获得结果。

"""
jieba的6个分词函数能够较高概率识别自定义的新词，比如名字或缩写。
对于无法识别的词也可以通过jieba.add_word()函数向分词库添加。
"""
print(jieba.lcut("某某同学在学Python"))
print(jieba.lcut("林某某在学Python"))
jieba.add_word("林某某")
print(jieba.lcut("林某某在学Python"))
