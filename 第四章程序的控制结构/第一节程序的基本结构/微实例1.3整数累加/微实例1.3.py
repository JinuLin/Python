# 微实例4.1.3整数累加
R = eval(input("请输入正整数："))
i, S = 0, 0
while i <= R:
    S = S + i
    i = i + 1
print("累加求和", S)
