# 微实例8.8.1CSV和JSON格式相互转换
"""
CSV格式常用于一二维数据表示和存储，JSON也可以表示一二维数据。
在网络信息传输中，可能需要统一表示方式，因此，需要在CSV和JSON格式间进行相互转换。
"""
import json

"""
将CSV转换成JSON格式
"""
fr = open("price2016.csv", "r", encoding='utf-8')  # 确保文件编码为utf-8
ls = []
for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(','))
fr.close()
fw = open("price2016.json", "w", encoding='utf-8')
for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))
    # zip()是一个内置函数，可以将两个长度相等的列表组合成一个关系对
json.dump(ls[1:], fw, sort_keys=True, indent=4, ensure_ascii=False)
#  ensure_ascii=False表示输出的json格式为中文，否则为ASCII码
fw.close()

"""
将JSON转换成CSV格式
"""
fr = open("price2016.json", "r", encoding='utf-8')
ls = json.load(fr)
data = [list(ls[0].keys())]
for item in ls:
    data.append(list(item.values()))
fr.close()
fw = open("price2016_from_json.csv", "w", encoding='utf-8')
for item in data:
    fw.write(",".join(item) + "\n")
fw.close()
