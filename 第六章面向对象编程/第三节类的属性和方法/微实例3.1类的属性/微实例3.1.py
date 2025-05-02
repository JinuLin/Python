# 微实例6.3.1类的属性
"""
实例属性和实例方法：通过“实例. 属性”和“实例. 方法”的方式访问属性和方法，被称为实例属性和实例方法。
类属性和类方法：相对于每个实例的属性和方法，类的所有实例共有的属性和方法称为类属性和类方法。
类属性是类所拥有的属性，在类中显式定义，类似于静态成员变量。
"""
class Hello(object):
	words = "Good morning!"
w = Hello()
print (w.words)                     		#通过实例访问
print (Hello.words)                		 #通过类进行访问
print ("-------------------------")
Hello.words = "Good afternoon!"     	#通过类进行修改
print (w.words)
print (Hello.words)
print ("-------------------------")
w.words = "Good night!"             	#通过实例修改
print (w.words)
print (Hello.words)
"""
类属性可以通过类或实例访问到，
通过类修改的属性值，修改的是类的属性值
通过实例修改的属性值仅仅修改了该实例的属性值，类的属性值不变
"""
