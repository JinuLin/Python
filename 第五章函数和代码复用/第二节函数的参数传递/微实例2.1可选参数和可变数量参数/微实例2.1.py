# 微实例5.2.1可选参数和可变数量参数
def dup(s, times=2):
    print(s * times)


dup("knock~")
dup("knock~", 4)


# 在定义函数时，可选参数必须定义在非可选参数之前，有些参数可以存在默认值，如果没有指定参数，则使用默认值。

def vfunc(a, *b):
    print(type(b))
    for n in b:
        a += n
    return a


print(vfunc(1, 2, 3, 4, 5))
# 在函数定义时，可以设计可变数量参数，通过参数前增加星号（*）实现。
# 输入的(2,3,4,5)被当做元组传递给b，与a累加后输出。
