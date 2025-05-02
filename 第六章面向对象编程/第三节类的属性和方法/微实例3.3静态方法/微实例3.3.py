# 微实例6.3.3静态方法
"""
静态方法是没有参数的方法。
由于静态方法既没有self参数，不能访问实例属性；又没有cls参数，也不能访问类属性。
所以静态方法跟定义它的类没有直接的关系，只是起到类似于函数的作用，一般用来存放逻辑性的代码。
静态方法的语法格式如下:
class 类名:
	@staticmethod
	def 静态类方法名():
		方法体
"""
#静态方法
import time
class TimeTest(object):
	def __init__(self,hour,minute,second):
		self.hour = hour
		self.minute = minute
		self.second = second
	@staticmethod               	#定义静态方法
	def showtime():
		return time.strftime("%H:%M:%S", time.localtime())
print (TimeTest.showtime()) 		#类名调用
t = TimeTest(2,10,10)
print (t.showtime())        		#实例调用
