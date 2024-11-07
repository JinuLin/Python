# 微实例6.3.1基本统计值计算
"""
getnum()函数从用户输入获得数据
mean()函数计算平均值
dev()函数计算标准差
median()函数计算中位数
"""
from math import sqrt

"""
getnum()函数循环从控制台获得用户输入的数字，
当用户按Enter键时退出所有数据保存在nums列表中。
列表nums初始化时定义为空，而后根据输入逐渐增加其长度。
"""


def getnum():  # 获取用户输入
    nums = []
    i_num_str = input("请输入数字(直接输入回车退出): ")
    while i_num_str != "":
        nums.append(eval(i_num_str))
        i_num_str = input("请输入数字(直接输入回车退出): ")
    return nums


"""
mean()函数用浮点数s记录列表numbers求和的结果。
其中，for语句表示从列麦numbers中取出每一个元素，
将其加到s变量中，直到numbers中的最后一个元素。
最后，通过return语句返回平均值，len(numbers)用于计算列表的长度。
"""


def mean(numbers):  # 计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)


"""
为了计算标准差，需要知道数据的平均值，由于mean()函数已经可以计算平均值，
将均值作为一个参数输入标准差dev()函数。
dev()函数中(val)**2用于计算val的平方，
sqrt(val)计算val的平方根。
"""


def dev(numbers, means):  # 计算方差
    s_dev = 0.0
    for num in numbers:
        s_dev = s_dev + (num - means) ** 2
    return sqrt(s_dev / (len(numbers) - 1))


"""
根据中位数的定义，
中位数函数median()首先使用Python内置函数sorted()对列表numbers进行排序，
然后根据中位数定义计算中位数。
"""


def median(numbers):  # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med


n = getnum()  # 主体函数
m = mean(n)
print("平均值:{},方差:{:.2},中位数:{}.".format(m, dev(n, m), median(n)))
"""
(1)列表是一个动态长度的数据结构，可以根据需求增加或减少元素；
(2)列表的一系列方法或操作符为计算提供了简单的元素运算手段；
(3)列表提供了对每个元素的简单访问方式及所有元素的遍历方式
"""
