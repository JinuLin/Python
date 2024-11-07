# 微实例4.7.2异常的高级用法
try:
    alp = "ABCDEFGHIJKLMNOPQRSTYVWSYZ"
    idx = eval(input("请输入一个整数："))
    print(alp[idx])
except NameError:
    print("输入错误，请输入一个整数")
except:
    print("其他错误")
"""
try-except支持多个except
try:
    <语句块1>
except <异常类型1>:
    <语句块2>
...
except <异常类型N>:
    <语句块N+1>
except:
    <语句块N+2>
except语句后面都指定了异常类型，最后一个except没有指定异常类型，可以处理其他的异常类型。
"""
