# 微实例4.7.1异常处理：try-except语句
try:
    num = eval(input("请输入一个整数："))
    print(num**2)
except NameError:
    print("输入错误，请输入一个整数！")
"""
运行错误时：
Traceback：异常回溯标记
NameError：异常类型，表示在程序中使用了一个未定义的变量或函数名，后面会跟着异常内容提示
采用try-except处理异常
try:
    <语句块1>
except <异常类型>:
    <语句块2>
"""
