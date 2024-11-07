# 微实例5.5.2字符串反转
def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]


n = input("请输入一个字符串：")
print(reverse(n))
"""
对于用户输入的字符串s，输出反转后的字符串。
解决这个问题的基本思想是把字符串看作一个递归对象。
"""
