# 微实例6.1.3类的构造方法和析构方法
"""
1.构造方法
构造方法（__init__）在创建对象时自动调用，用于初始化对象的属性。
它通常用于设置对象的初始状态或执行一些必要的初始化操作。
例如，在创建Car对象时，构造方法会自动将color属性设置为"白色"。
"""


class Car:
    # 构造方法
    def __init__(self):
        self.color = "白色"

    # 成员方法
    def run(self):
        print("{}的小汽车在跑".format(self.color))


# 创建对象
my_car = Car()
# 调用方法
my_car.run()

"""
2.析构方法
析构方法（__del__）在对象被销毁时自动调用，用于释放对象占用的资源或执行一些清理操作。
它通常用于关闭文件、释放内存等操作。
例如，在删除Person对象时，析构方法会自动打印一条消息，表示该对象的资源已被释放。
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # 析构方法
    def __del__(self):
        print("释放{}这个对象的资源".format(self.name))

# 实例化对象
p = Person("小明",18)
# 释放对象
del p
