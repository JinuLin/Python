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
