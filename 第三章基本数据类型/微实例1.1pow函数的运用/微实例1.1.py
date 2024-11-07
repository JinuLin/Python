# 3.1.1微实例pow函数的运用
import sys

sys.set_int_max_str_digits(0)
# 第三个程序输出会超过限制4300，所以引用sys当中的set_int_max_str_digits(0)来取消限制
A = pow(2, 100)  # pow是python的内置函数，pow(x，y)表示运算x^y
B = pow(2, 500)
C = pow(2, pow(2, 15))  # 可以嵌套使用

print("{}".format(A))
print("{}".format(B))
print("{}".format(C))
