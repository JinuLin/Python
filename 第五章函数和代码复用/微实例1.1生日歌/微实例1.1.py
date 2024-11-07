# 微实例5.1.1生日歌
def happy():
    print("Happy birthday to you!")


def happyB(name):
    happy()
    happy()
    print("Happy birthday, dear {}!".format(name))
    happy()


happyB("Mike")
print()
happyB("Lily")
"""
def函数可以于函数的定义与复用
def <函数名>(<参数列表>):
# 函数名可以是任何有效的Python标识符
# 参数列表是调用函数时传递给它们的值，可以是零个、一个、多个，多个时用逗号隔开，没有参数时保留括号。
# 这里的参数是形式参数，简称“形参”。
    <函数体>  # 调用时执行的代码。
    return <返回值列表>
    # 当需要返回值时使用return和返回值列表，否则可以没有，函数体结束控制权返回给调用者。
函数调用和执行的一般形式如下：
<函数名>(<参数列表>)
此时，参数列表要传入函数内部的参数，这类参数被称为实际参数，简称为“实参”。
"""
