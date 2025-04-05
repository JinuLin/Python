# 微实例3.2.3数字类型的转换
a = int(4.5)  # int(x) 将x转换为整数，x可以是浮点数或字符串
b = float(4)  # float(x) 将x转换为浮点数，x可以是整数或字符串
c = complex(4)  # complex(re[, im]) 生成一个复数，实部为re，虚部为im，re可以是整数、浮点数或字符串，im可以是整数或浮点数但不能为字符串
print("{}".format(a))  # 去掉小数转换为浮点数
print("{}".format(b))  # 增加小数转换为整数
print("{}".format(c))  # 增加虚数部分转换为复数
z = 4.5 + 0j
print(type(4.5))
print(type(z))  # type是一个判断数字类型的函数
