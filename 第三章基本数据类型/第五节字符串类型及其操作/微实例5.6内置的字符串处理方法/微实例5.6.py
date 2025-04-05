# 微实例3.5.6内置的字符串处理方法
# str.lower() 返回字符串str的副本，全部字符小写
# str.upper() 返回字符串str的副本，全部字符大写
# str.islower() 当str所有字符都是小写时，返回True，否则False
# str.isprintable() 当str所有字符都是可打印的，返回True，否则False
# str. isnumeric() 当str所有字符都是字符时，返回True，否则False
# str.isspace() 当str所有字符都是空格，返回True，否则False
# str.endswith(suffix[,start[,end]]) str[start: end] 以suffix结尾返回True，否则返回False
# str.startswith(prefix[, start[, end]]) str[start: end] 以suffix开始返回True，否则返回False
# str.split(sep=None, maxsplit=-1) 返回一个列表，由str根据sep被分割的部分构成，默认分隔符为空，maxsplit为切割次数，可以默认不给出
# str.count(sub[,start[,end]]) 返回str[start: end]中sub子串出现的次数
# str.replace(old, new[, count]) 返回字符串str的副本，所有old子串被替换为new，如果count给出，则前count次old出现被替换
# str.center(width[, fillchar]) 字符串居中函数，返回长度为width中的字符串，其中，str处于新字符串中心位置，两侧用fillchar填充。如果width小于字符串，则返回str
# str.strip([chars]) 返回字符串str的副本，在其左侧和右侧去掉chars中列出的字符
# str.zfill(width) 返回字符串str的副本，长度为width，不足部分在左侧添0
# str.format() 返回字符串str的一种排版格式
# str.join(iterable) 返回一个新字符串，由组合数据类型iterable变量的每个元素组成，元素间用str分割

print(hex(255))
print(oct(-255))
print("Python is excellent language.".split())
print("PYTHON".center(40, '='))
print("123".zfill(40))
print("-123".zfill(40))
