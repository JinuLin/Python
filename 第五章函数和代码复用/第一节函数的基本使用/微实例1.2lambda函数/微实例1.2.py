# 微实例5.1.2lambda函数
f = lambda x, y: x + y
print(type(f))
print(f(10, 12))
"""
lambda函数称之为匿名函数，将函数名作为函数结果返回
<函数名> = lambda <参数列表>: <表达式>
等价于
def <函数名>(<参数列表>):
    return <表达式>
"""
