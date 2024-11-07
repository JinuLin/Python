# python 中合法的数字有十进制整数，浮点数，十六进制整数，复数
# --------------------------3 也是合法数字
def isNum(num):
    np = '+-'
    numbers = '.0123456789'
    numbersE = '.0123456789+-jJEe'
    x16 = '0123456789abcdefABCDEF'
    if num[0] in np:
        try:
            return isNum(num[1:])
        except:
            return False
    elif num[0] in numbers:
        if num[:2] == '0x':  # 16 进制分支
            for i in num[2:]:
                if i not in x16:
                    return False
            return True
        else:
            ele = 0
            point = 0
            last = ''
            numaftere = 0
            q = 0
            for i in num:
                q = q + 1
                if i not in numbersE:
                    return False
                else:
                    if point == 0 and i == '.':
                        point = 1
                        continue
                    if point == 1 and (numaftere == 1 or ele == 0) and i in '+-':  # 一个数字结束，进入了第二个数字(一般是复数)
                        point = 0
                        continue
                    if ele == 0 and i in 'Ee':  # 出现了第一个 E， 一个浮点数中只能出现一个E
                        ele = 1
                        continue
                    if ele == 1 and i in '0123456789':
                        numaftere = 1
                        continue
                    if ele == 1 and numaftere == 1 and i in '+-':  # 针对复数的特例
                        ele = 0
                        numaftere = 0
                        continue
                    if last == '.' and i in '+-':
                        return False
                    elif (point == 1 or last in 'EeJj') and i == '.':
                        return False
                    elif i in 'Jj' and last in '+-':
                        return False
                    elif ele == 1 and i in 'Ee.':
                        return False
                last = i
            if last == '.' and i in '+-':
                return False
            elif (point == 1 or last in 'EeJj') and i == '.':
                return False
            elif i in 'Jj' and last in '+-.':
                return False
            elif ele == 1 and i in 'Ee.':
                return False
            else:
                return True
    else:
        return False


# 测试集
print(isNum('Hello'))  # False
print(isNum('+++++++++++++++++++++++++++++++++++++'))  # False
print(isNum('+-+-+-+-+-+-3'))  # True
print(isNum('100'))  # True
print(isNum('10e10'))  # True
print(isNum('10e+10'))  # True
print(isNum('10e10.'))  # True
print(isNum('10e10e'))  # False
print(isNum('10e10+4E10'))  # True
print(isNum('10e'))  # False
print(isNum('10e+1j'))  # True
print(isNum('10e10+1.j'))  # True
print(isNum('1.0e+10-j'))  # True
print(isNum('1.0e+1j-3.e'))  # True
print(isNum('1.0e10+1j-3.e10'))  # False
print(isNum('1.3333'))  # True
print(isNum('.3333'))  # True
print(isNum('.333.3'))  # True
print(isNum('.3333e5'))  # True
print(isNum('12345678'))  # True
print(isNum('0abddf'))  # False
print(isNum('0xabddf'))  # True
