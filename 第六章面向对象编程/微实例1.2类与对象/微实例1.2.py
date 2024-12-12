# 微实例6.1.2类与对象
"""
类：具有相同特征和行为的事物的统称
属性：描述事物的特征
方法：描述事物的行为
可以用关键字class声明一个类
"""


class Car:
    @staticmethod  # 静态方法，用修饰符staticmethod声明
    def run():
        print('汽车在跑')


"""
类定义好后，可以根据这个类创建一个对象
对象名 = 类名()  # 创建对象
对象名.新的属性名 = 值  # 添加属性
对象名.方法名()  # 调用方法
"""
my_car = Car()  # 创建对象
my_car.color = 'red'  # 添加属性
print(my_car.color)  # 访问属性
my_car.run()  # 调用方法
