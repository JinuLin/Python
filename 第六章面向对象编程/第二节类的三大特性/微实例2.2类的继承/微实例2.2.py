# 微实例5.2.2类的继承
"""
类的继承是指在现有的类基础上，再定义新的类，新的类称为子类，
而现有类称为父类，子类继承了父类的所有属性和方法。
继承可以分为单继承和多继承。
"""
"""
单继承是指子类从唯一的父类继承属性和方法。
语法为：class 子类名(父类名):
"""


# 定义父类
class Grandpa(object):  # 如果定义类的时候没有写父类，默认继承object类
    def __init__(self, color):
        self.color = color

    def description(self):
        print('我的颜色是%s' % self.color)


# 定义子类

class Square(Grandpa):
    pass


# 创建子类对象
s = Square('黄色')
s.description()
"""
子类没有定义任何属性和方法，但是它继承了父类，所以能调用description。
"""
"""
子类可以根据需要改变继承自父类的方法，即重写父类方法。
"""


class Square(Grandpa):
    def description(self):
        print('我的颜色是%s,我是正方形' % self.color)


s = Square('黄色')
s.description()

"""
父类的私有属性和私有方法不会被子类继承，更不能被子类访问。
"""
"""
例如以下代码：
class Grandpa(object):
    def __init__(self, color):
        self.__color = color

    def description(self):
        print('我的颜色是%s的图形' % self.__color)

    def __description(self):
        print(self.__color)


class Square(Grandpa):
    def test(self):
        print(self.__color)
        self.__description()


s = Square('黄色')
s.description()
s.test()

会有报错：
Traceback (most recent call last):
    s.test()
    ~~~~~~^^
    print(self.__color)
          ^^^^^^^^^^^^
AttributeError: 'Square' object has no attribute '_Square__color'
说明：父类的私有属性和私有方法不会被子类继承，更不能被子类访问。
"""

"""
多继承是指子类从多个父类继承属性和方法。
语法为：class 子类名(父类名1,父类名2,父类名3,...):
"""
#  定义马的类
class Horse(object):
    @staticmethod
    def run():
        print('-----我会跑-----')

    @staticmethod
    def eat():
        print('-----我会吃草-----')
#  定义鸟的类
class Bird(object):
    @staticmethod
    def fly():
        print('-----我会飞-----')

    @staticmethod
    def eat():
        print('-----我会吃虫-----')

#  定义飞马的类
class FlyHorse(Horse, Bird):
    pass

fh = FlyHorse()
fh.run()
fh.fly()

"""
如果多继承性父类中有同名方法时，在Python 3中，子类先继承哪个类会先调用哪个类的方法。
"""
fh.eat()
"""
如果当前父类非常复杂，Python会使用mro算法找到合适的类，来确定执行哪个类。
"""

"""

"""