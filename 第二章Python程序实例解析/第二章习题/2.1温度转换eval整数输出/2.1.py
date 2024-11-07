TempStr = input("请输入带有符号的温度值: ")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8  # eval函数用来执行一个字符串表达式，并返回表达式的值，可以将字符串转化成其他变量类型。
    # 语法eval(expression[, globals[, locals]])
    # expression – 表达式。
    # globals – 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
    # locals – 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
    print("转换后的温度是{}C".format(int(C)))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * (eval(TempStr[0:-1])) + 32
    print("转换后的温度是{}F".format(int(F)))
else:
    print("输入格式错误")
