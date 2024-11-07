# 微实例4.7.3异常语句与else和finally配合使用
try:
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idx = eval(input("请输入一个整数: "))
    print(alp[idx])
except NameError:
    print("输入错误，请输入一个整数!")
else:
    print("没有发生异常")
finally:
    print("程序执行完毕，不知道是否发生了异常")
"""
try-except保留字可以搭配else和finally使用
try:
    <语句块1>
except <异常类型1>:
    <语句块2>
else:
    <语句块3>
finally:
    <语句块4>
当没有异常时，执行完try中的语句块时，才会执行else中的语句块。
无论程序是否有异常，一定会执行finally。
"""