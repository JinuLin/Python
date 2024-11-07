def isPrime(num):
    import math
    try:
        if type(num) is type(0.):
            raise TypeError
        r = int(math.floor(math.sqrt(num)))
    except TypeError:
        print('不是一个有效的整数')
        return None
    if num == 1:
        return False
    for i in range(2, r + 1):
        if num % i == 0:
            return False
    return True


# 测试集
print(isPrime(2))
print(isPrime(44))
print(isPrime('str'))
print(isPrime(1))
print(isPrime(3.3))
print(isPrime(0x18))
