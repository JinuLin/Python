def isOdd(num):
    try:
        if type(num) is type(0.):
            raise TypeError
        if num % 2 == 0:
            return False
        else:
            return True
    except TypeError:
        print("这不是一个有效的整数！")


print(isOdd(4))
print(isOdd(3))
print(isOdd(-1))
print(isOdd('str'))
print(isOdd(3.))
