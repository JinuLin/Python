# 微实例5.3.2datetime库解析
from datetime import datetime, timezone

"""
1.使用datetime.now()获得当前日期和时间对象，使用方法如下：
datetime.now()
作用：返回一个datetime类型，表示当前的日期和时间，精确到微秒。
"""
today = datetime.now()
print(today)

"""
2.使用datetime.utcnow()获得当前日期和时间对应的UTC（世界标准时间）时间对象，使用方法如下：
datetime.utcnow()
作用：返回datetime类型，表示当前日期和时间的UTC表示，精确到微秒。
在未来版本的 Python 中将移除 datetime.datetime.utcnow() 的使用
并建议使用具有时区意识的对象来表示 UTC 时间。
可以用today = datetime.now(timezone.utc)获取到带有正确时区信息的当前UTC时间。
"""
today = datetime.now(timezone.utc)
print(today)

"""
3.datetime.now() 和 datetime.utcnow()都返回一个datetime类型的对象,
也可以直接使用datetime()构造一个日期和时间对象，使用方法如下：
datetime(year（年份）, month（月份）, day（日期）, hour=0（小时）, minute=0（分钟数）,second=0（秒数）,microsecond=0（微秒数）)
作用：返回一个datetime类型，表示指定的日期和时间，可以精确到微秒。
其中，hour,minute,second,microsecond参数可以全部或部分省略
"""
# 调用datetime()函数直接创建一个datetime对象，表示2016年9月16日22:33，32秒7微秒
someday = datetime(2016, 9, 16, 22, 33, 32, 7)
print(someday)
# 程序已经有了一个datetime对象，进一步可以利用这个对象的属性显示时间，
# 为了区别datetime库名，采用上例中的someday代替生成的datetime对象

"""
datetime类的9个常用属性
someday.min 固定返回datetime 的最小时间对象，datetime(1,1,1,0,0)
someday.max 固定返回datetime的最大时间对象，datetime(9999,12,31,23,59,59,999999)
someday.year 返回someday包含的年份
someday.month 返回someday包含的月份
someday.day 返回someday包含的日期
someday.hour 返回someday包含的小时
someday.minute 返回someday包含的分钟
someday.second 返回someday包含的秒钟
someday.microsecond 返回someday包含的微秒值
"""

"""
datetime类的3个常用时间格式化方法
someday.isoformat() 采用ISO 8601标准显示时间
someday.isoweekday() 根据日期计算星期后返回1-7,对应星期一到星期日
someday.strftime(format) 根据格式化字符串format进行格式显示的方法
"""
# isoformat()和isoweekday()方法的使用
someday = datetime(2016, 9, 16, 22, 33, 32, 7)
print(someday.isoformat())
print(someday.isoweekday())

# strftime()方法是时间格式化最有效的方法，几乎可以以任何通用格式输出时间
print(someday.strftime("%Y-%m-%d %H:%M:%S"))
"""
strftime()方法的格式化控制符
%Y 年份 0001~9999，例如：1900
%m 月份 01~12，例如：10
%B 月名 January~December，例如：April
%b 月名缩写 Jan~Dec，例如：Apr
%d 日期 01 ~ 31，例如：25
%A 星期 Monday~Sunday，例如：Wednesday
%a 星期缩写 Mon~Sun，例如：Wed
%H 小时（24h制） 00 ~ 23，例如：12
%I 小时（12h制） 01 ~ 12，例如：7
%p 上/下午 AM, PM，例如：PM
%M 分钟 00 ~ 59，例如：26
%S 秒 00 ~ 59，例如：26
"""
now = datetime.now()
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%A, %d. %B %Y %I:%M%p"))
# strftime()格式化字符串的数字左侧会自动补零
print("今天是{0:%Y}年{0:%m}月{0:%d}日".format(now))  # 也可以与print()的格式化函数一起使用
