# 微实例8.4.3一二维数据的表示与读写
"""
CSV文件的每一行是一维数据，可以使用Python中的列表类型表示，
整个CSV文件是一个二维数据，由表示每一行的列表类型作为元素，组成一个二维列表。
"""
fo = open("price2016.csv", "r")
ls = []
for line in fo:
    """
    需要注意，以split(",")方法从CSV文件中获得内容时，
    每行最后一个元素后面包含了一个换行符（"\n"）。
    对于数据的表达和使用来说，这个换行符是多余的，可以通过使用字符串的replace()方法将其去掉
    """
    line = line.replace("\n", "")
    ls.append(line.split(","))
print(ls)
fo.close()

"""
逐行处理CSV格式数据
"""
fo = open("price2016.csv", "r")
ls = []
for line in fo:
    line = line.replace("\n", "")
    ls = line.split(",")
    lns = ""
    for s in ls:
        lns += "{}\t".format(s)
    print(lns)
fo.close()

"""
一维数据写入CSV文件
"""
"""
对于Python列表变量保存的一维数据结果，
可以用字符串的join()方法组成逗号分隔形式再通过文件的write()方法储存到CSV文件中
"""
fo = open("price2016bj.csv", "w")
ls = [' 北 京 ', '101.5', '120.7', '121.4']
fo.write(",".join(ls) + "\n")
# 其中，",".join()方法生成一个字符串，由字符串","分隔列表中的元素形成
fo.close()

"""
二维数据写入CSV文件
"""
"""
对于二维数据，
可以使用嵌套循环，
将二维列表中的每一个元素都用字符串的join()方法组成逗号分隔形式再通过文件的write()方法储存到CSV文件中。
样式如下：
for row in ls:
<输出文件>.write(",".join(row)+"\n")
"""
fr = open("price2016.csv", "r")
fw = open("price2016out.csv", "w")
ls = []
for line in fr:  # 将CSV文件中的二维数据读入到列表变量
    line = line.replace("\n", "")
    ls.append(line.split(","))
    for i in range(len(ls)):  # 遍历列表变量计算百分数
        for j in range(len(ls[i])):
            if ls[i][j].replace(".", "").isnumeric():
                ls[i][j] = "{:.2}%".format(float(ls[i][j]) / 100)
for row in ls:  # 将列表变量中的二位数据输出到CSV文件
    print(row)
    fw.write(",".join(row) + "\n")
fr.close()
fw.close()
