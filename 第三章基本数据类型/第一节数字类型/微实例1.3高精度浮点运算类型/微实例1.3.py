# 微实例3.1.3高精度浮点数运算类型
import decimal  # decimal提供了更精确的数字类型Decimal

a = decimal.Decimal('3.1415929')
b = decimal.Decimal('1.23456789')
decimal.getcontext().prec = 20  # getcontext().prec = x (x为你想要的精度来设置)
c = a * b
print("{}".format(c))
