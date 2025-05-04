# 微实例8.8.1CSV和JSON格式相互转换
"""
CSV格式常用于一二维数据表示和存储，JSON也可以表示一二维数据。
在网络信息传输中，可能需要统一表示方式，因此，需要在CSV和JSON格式间进行相互转换。
"""
import json

"""
将CSV转换成JSON格式
"""
fr = open("price2016.csv", "r")
ls = []
for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(','))
fr.close()
fw = open("price2016.json", "w")
for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))
json.dump(ls[1:], fw, sort_keys=True, indent=4)
fw.close()
