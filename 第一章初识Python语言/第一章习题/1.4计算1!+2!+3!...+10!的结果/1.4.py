# 1.4计算1+2!+3!+...+10!的结果
sum, tmp = 0, 1
for i in range(1, 11):
    tmp *= i
    sum += tmp
print("运算结果是: {}".format(sum))
