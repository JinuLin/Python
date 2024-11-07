# 微实例4.5.1random库的用法
from random import *

"""
seed(a=None) 初始化随机数种子，默认值为当前系统时间
random() 生成一个[0.0, 1.0)之间的随机小数
randint(a, b) 生成一个[a,b]之间的整数
getrandbits(k) 生成一个k比特长度的随机整数
randrange(start, stop[, step]) 生成一个[start, stop)之间以step为步数的随机整数
uniform(a, b) 生成一个[a, b]之间的随机小数
choice(seq) 从序列类型(例如：列表)中随机返回一个元素
shuffle(seq) 将序列类型中元素随机排列，返回打乱后的序列
sample(pop, k) 从pop类型中随机选取k个元素，以列表类型返回
"""
print(random())

print(uniform(1, 10))

print(uniform(1, 20))

print(randrange(0, 100, 4))  # 从0开始到100以4递增的元素中随机返回

print(choice(range(100)))

ls = list(range(10))
print(ls)

shuffle(ls)
print(ls)

# 生成随机数之前可以通过seed()函数指定随机数种子
# 随机种子一般是一个整数，只要种子相同，每次生成的随机数序列也相同
# 这种情况便于测试和同步数据
seed(125)  # 随机种子赋值为125
print("{}.{}.{}".format(randint(1, 10), randint(1, 10), randint(1, 10)))
print("{}.{}.{}".format(randint(1, 10), randint(1, 10), randint(1, 10)))
seed(125)  # 再次给随机种子赋值为125
print("{}.{}.{}".format(randint(1, 10), randint(1, 10), randint(1, 10)))
