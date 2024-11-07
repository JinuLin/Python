# 微实例3.4.1天天向上
"""
一年365天，以第1天的能力值为基数，记为1.0，当好好学习时能力值相比前一天提高1%，当没有学习时由于遗忘等原因能力值相比前一天下降1‰。
每天努力和每天放任，一年下来的能力值相差多少?
"""
import math

dayup = math.pow((1.0 + 0.001), 365)  # 调高0.001
daydown = math.pow((1.0 - 0.001), 365)  # 放任0.001
print("向上:{:.2f},向下:{:.2f}.".format(dayup, daydown))

"""
一年365天，如果好好学习时能力值相比前一天提高5%，当放任时相比前一天下降5%。效果相差多少呢?
"""

dayup = math.pow((1.0 + 0.005), 365)  # 提高0.005
daydown = math.pow((1.0 - 0.005), 365)  # 放任0.005
print(" 向 上 : {:.2f}, 向 下 : {:.2f}.".format(dayup, daydown))

"""
一年365天，如果好好学习时能力值相比前一天提高1%，当放任时相比前一天下降1%。效果相差多少呢?
"""
dayfactor = 0.01
dayup = math.pow((1.0 + dayfactor), 365)  # 提 高dayfactor
daydown = math.pow((1.0 - dayfactor), 365)  # 放 任dayfactor
print(" 向 上 : {:.2f}, 向 下 : {:.2f}.".format(dayup, daydown))

"""
一年365天，一周5个工作日，如果每个工作日都很努力，可以提高1%，仅在周末放任一下，能力值每天下降1%，效果如何呢？
"""
dayup, dayfactor = 1.0, 0.01
for i in range(365):
    if i % 7 in [6, 0]:  # 周六周日
        dayup = dayup * (1 - dayfactor)
else:
    dayup = dayup * (1 + dayfactor)
print("向上5天向下2天的力量: {:.2f}.".format(dayup))

"""
每周工作5天，休息2天，休息日水平下降0.01，工作日要努力到什么程度一年后的水平才与每天努力1%所取得的效果一样呢？
"""


def dayUP(df):
    Dayup = 1.0
    for n in range(365):
        if n % 7 in [6, 0]:
            Dayup = Dayup * (1 - 0.01)
        else:
            Dayup = Dayup * (1 + df)
    return Dayup


dayfacotr = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("每天的努力参数是: {:.3f}.".format(dayfactor))
