# 微实例2.1.3温度转换封装
def tempConvert(ValueStr):
    if ValueStr[-1] in ['F', 'f']:
        C = (eval(ValueStr[0:-1]) - 32) / 1.812
        print("转换后的温度是{:.2f}C".format(C))
    elif ValueStr[-1] in ['C', 'c']:
        F = 1.8 * eval(ValueStr[0:-1]) + 32
        print("转换后的温度是{:.2f}F".format(F))
    else:
        print("输入格式错误")


TempStr = input("请输入带有符号的温度值: ")
tempConvert(TempStr)
