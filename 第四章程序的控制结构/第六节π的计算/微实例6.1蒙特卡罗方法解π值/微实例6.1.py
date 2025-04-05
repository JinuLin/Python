# 微实例4.6.1蒙特卡罗方法解π值
from random import random
from math import sqrt
from time import perf_counter
DARTS = 1000  # 表示抛点数，抛点数越大运行时间越长，数值越精确。
hits = 0.0
t = perf_counter()/100000
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("pi的值是{}.".format(pi))
print("运行时间是{:.5f}s".format(t))
