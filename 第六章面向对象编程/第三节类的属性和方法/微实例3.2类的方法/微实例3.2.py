# 微实例6.3.2类的方法
"""
类方法定义的语法格式：
class 类名:
	@classmethod
	def 类方法名(cls):
		方法体
其中@classmethod是标识类方法的修饰器,只有带了这个修饰器的方法才是类方法。
类方法的第一个参数是cls。
区别于self代表实例本身,cls代表定义类方法的类。
类方法可以由类进行调用,也可以由实例对象进行调用。
"""
class Person(object):
	count = 0       #类属性
	@classmethod    #类方法
	def display_count(cls):
		print ("总人数为%d" % cls.count)
	def __init__(self,name):    #实例方法
		self.name = name        #实例属性
		Person.count = Person.count + 1     #修改类属性值
		print('-----Insert Jon-------')
p1 = Person('Jon')
Person.display_count()   	#类调用类方法
p1.display_count()       	#实例调用类方法
print('-----Insert Lily------')
p2 = Person('Lily')
Person.display_count()   	#类调用类方法
p1.display_count()       	#实例调用类方法
p2.display_count()       	#实例调用类方法
