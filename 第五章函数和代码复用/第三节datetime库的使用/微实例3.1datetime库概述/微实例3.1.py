# 微实例5.3.1datetime库概述
from datetime import datetime
# datetime库可以从系统中获得时间，并以用户选择的格式输出。
now = datetime.now()
print(now)
"""
datetime库以类的方式提供多种日期和时间表达方式：
 datetime.date：日期表示类，可以表示年、月、日等
 datetime.time：时间表示类，可以表示小时、分钟、秒、毫秒等
 datetime.datetime：日期和时间表示的类，功能覆盖date和time类
 datetime.timedelta：时间间隔有关的类
 datetime.tzinfo：与时区有关的信息表示类
"""
