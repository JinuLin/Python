# 微实例1.1.5日期和时间的输出
from datetime import datetime  # 引用datetime 库

now = datetime.now()  # 获得当前日期和时间信息
print(now)
print("{}".format(now.strftime("%x")))  # 输出其中的日期部分
print("{}".format(now.strftime("%X")))  # 输出其中的时间部分
