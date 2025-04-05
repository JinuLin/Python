# 微实例6.1.3类的构造方法和析构方法
"""
1.构造法
可以使用__init__()方法，在创建对象时就添加好属性
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
2.析构法
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
