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