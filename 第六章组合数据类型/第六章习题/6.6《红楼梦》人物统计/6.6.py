import jieba.posseg as ps

txt = open('红楼梦.txt', 'r', encoding='utf-8').read()
# exclude = ['什么','那里','一个','我们','你们','如今','说到','知道','起来','众人','他们','太太','只见','怎么',]
exclude = ['明白', '探春']
counts = {}


def count_figures():
    words = ps.cut(txt)
    for w in words:
        if len(w.word) == 1:
            continue
        if w.flag == 'nr':
            counts[w.word] = counts.get(w.word, 0) + 1
    for key in exclude:
        del (counts[key])
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(20):
        word, count = items[i]
        print('{0:<10}{1:>5}'.format(word, count))


count_figures()
