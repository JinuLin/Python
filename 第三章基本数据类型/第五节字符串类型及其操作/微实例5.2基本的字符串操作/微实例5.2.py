# 微实例3.5.2基本的字符串操作
# x+y 连接两个字符串x与y
# x,y 连接两个字符串x与y
# x*n或n*x 复制n次字符串x
# x in s 如果x是s的子串，返回True，否则返回False
# str[i] 索引，返回第i个字符
# str[N:M] 切片，返回索引第N到第M的子串，其中不包含M
print("Python语言" + "程序设计")
print("Python语言", "程序设计")
name = "Python语言" + "程序设计" + "基础"
print(name)
print("GOAL!" * 3)
print("Python语言" in name)
print("Y" in "Python语言")
# len函数可以返回一个字符串的长度
print(len("Python"))
