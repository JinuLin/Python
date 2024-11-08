from random import *


def randbirth():
    mon = randint(1, 12)
    if mon in [1, 3, 5, 7, 8, 10, 12]:
        day = randint(1, 31)
    elif mon == 2:
        day = randint(1, 28)
    else:
        day = randint(1, 30)
    return mon * 100 + day


def randnum(person_num):
    ls = []
    for a in range(person_num):
        ls.append(randbirth())
    if len(ls) == len(set(ls)):
        return False
    else:
        return True


try:
    personnum = eval(input("请输入房间人数："))
    poss = 0
    mean = 0.0
    for n in range(1000, 11000, 1000):
        for i in range(n):
            if randnum(personnum):
                poss += 1
        mean += poss * 100 / n
        poss = 0
    print("当房间内的人数为{}时，至少有两个人生日相同的几率是{:.2f}%。".format(personnum, mean / 10))

except ValueError as e:
    print(f"输入错误: {e}")
except Exception as e:
    print(f"发生未知错误: {e}")
