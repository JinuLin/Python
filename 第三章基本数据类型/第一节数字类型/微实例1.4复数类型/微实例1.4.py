# 微实例3.1.4复数类型
z = 1.23e-4 + 5.6e+89j  # 表示复数z（a+bj）的计算
a = z.real  # .real表示提取实数部分
b = z.imag  # .imag表示提取虚数部分
print("实部为{}".format(a))
print("虚部为{}".format(b))
