i = input("请输入金额用“￥”或“$”结束：")
if i[-1] in ['￥']:
    C = (eval(i[0:-1])) / 6
    print("转换后是{:.2f}美元".format(C))
elif i[-1] in ['$']:
    F = (eval(i[0:-1])) * 6
    print("转换后是{:.2f}元".format(F))
else:
    print("输入格式错误")
