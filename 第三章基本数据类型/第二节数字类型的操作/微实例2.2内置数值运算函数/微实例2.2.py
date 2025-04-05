# 微实例3.2.2内置数值运算函数
# abs(x) x的绝对值
# divmod(x, y) (x//y, x%y)，输出为二元组形式（也称为元组类型）
# pow(x, y[, z]) (x**y)%z，[..]表示该参数可以省略，即：pow(x,y)，它与x**y相同
# round(x[, ndigits]) 对x四舍五入，保留ndigits位小数。round(x)返回四舍五入的整数值
# max(x1, x2, …, xn) x1, x2, …, xn的最大值，n没有限定
# min(x1, x2, …, xn) x1, x2, …, xn的最小值，n没有限定
a = abs(-3 + 4j)  # abs可以计算复数的绝对值
print("{}".format(a))
b = pow(3, pow(3, 999), 10000)  # 等价于pow(3, pow(3, 999))%10000，即可以幂运算与模运算同时进行。
print("{}".format(b))
