def multi(*args):
    sums = 1
    count = 1
    for i in args:
        if type(i) is type(1) or type(i) is type(1.):
            sums *= i
        else:
            print('第{}项不是一个有效的整数！'.format(count))
            return
        count += 1
    return sums


print(multi(2, 3, 1.0, 5, 4.99))
print(multi(2, 1, 'str'))

# 测试集
mun = multi(1, 2, 3, 4, 5, 6)
print(mun)
