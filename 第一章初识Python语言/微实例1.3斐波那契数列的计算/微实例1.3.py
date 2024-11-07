# 微实例1.1.3斐波那契数列的计算
a, b = 0, 1
while a < 1000:  # 输出不大于1000 的序列。while表示循环
    print(a, end=',')
    a, b = b, a + b
