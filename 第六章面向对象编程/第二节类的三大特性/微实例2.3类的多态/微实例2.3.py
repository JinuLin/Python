# 微实例6.2.3类的多态
"""
在 Python中，多态指不考虑对象类型的情况下使用对象。
Python推崇“鸭子类型”。
“鸭子类型”是这样描述的：如果看到的动物走起来像鸭子，游泳起来像鸭子，叫起来也像鸭子，
那么这只动物就可以被称为鸭子。
"""
#定义一个动物类
class Animal(object):
	def shout(self):    #叫的方法
		print("-------动物在叫-------")
#定义一个猫的类
class Cat(Animal):
	def shout(self):
		print("-------喵喵-------")
#定义一个狗的类
class Dog(Animal):
	def shout(self):
		print("-------汪汪-------")
#定义一个函数
def func(temp):
	temp.shout()
dog = Dog()
func(dog)
cat = Cat()
func(cat)
"""
因为func()函数的参数temp并没有指定类型，
所以如果传入其他类型的对象也是可以的，只要该对象具有shout() 方法，而不一定要继承自 Animal。
比如在代码中增加一个Train类，类中也定义shout()方法
"""
class Train(Animal):
	def shout(self):
		print("-------呜呜-------")

train = Train()
func(train)
