str_i = input("请输入您想要的字符串：")
kong = 0
alpha = 0
chi = 0
num = 0
other = 0
for i in str_i:
    if i == " ":  # 判断空格
        kong += 1
    elif '0' <= i <= '9':  # 判断数字
        num += 1
    elif u'\u4e00' <= i <= u'\u9fa5':  # 判断中文
        # Unicode中文字符的码点范围是从 u'\u4e00' 到 u'\u9fa5'u'\u4e00'
        chi += 1
    elif i.isalpha():  # 判断英文
        # isalpha()函数用于检测字符串是否只包含字母，是则返回 True，否则返回 False。
        alpha += 1
    else:  # 判断其他字符
        other += 1
print("您输入的字符串中有{}个空格,{}个数字,{}个中文,{}个英文字符,{}个其他字符".format(kong, num, chi, alpha, other))
# 可以使用string库，或可以先建立列表然后进行判断。
