# 微实例5.2.3函数的返回值
def func(a, b):
    return a * b  # return语句用来退出函数并将程序返回到函数被调用的位置继续执行。


# return语句同时可以将0个、1个或多个函数运算完的结果返回给函数被调用处的变量。


s = func("knock~", 2)
print(s)


# 函数可以没有return，此时函数并不返回值。

def func(a, b):
    return b, a
# 函数也可以用return返回多个值，多个值以元组类型保存


s = func("knock~", 2)
print(s, type(s))
