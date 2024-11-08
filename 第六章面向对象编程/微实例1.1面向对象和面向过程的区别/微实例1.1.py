# 微实例6.1.1面向对象和面向过程的区别
# 定义一个函数来计算矩形的面积
def calculate_area(length0, width0):
    return length0 * width0


# 定义一个函数来计算矩形的周长
def calculate_perimeter(length0, width0):
    return 2 * (length0 + width0)


# 主程序部分
length = 5
width = 3

# 调用函数计算面积和周长
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

# 输出结果
print(f"面向过程 - 矩形的面积: {area}")
print(f"面向过程 - 矩形的周长: {perimeter}")


# 定义一个矩形类
class Rectangle:
    def __init__(self, length0, width0):
        self.length = length0
        self.width = width0

    # 定义一个方法来计算矩形的面积
    def calculate_area(self):
        return self.length * self.width

    # 定义一个方法来计算矩形的周长
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# 创建一个矩形对象
rectangle = Rectangle(5, 3)

# 调用对象的方法计算面积和周长
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

# 输出结果
print(f"面向对象 - 矩形的面积: {area}")
print(f"面向对象 - 矩形的周长: {perimeter}")

'''
1.结构化 vs 封装：
面向过程：程序被分解为一系列函数，数据和函数是分开的。这种方式更注重过程，即解决问题的步骤。
面向对象：程序被分解为对象，每个对象封装了数据（属性）和操作这些数据的方法。这种方式更注重对象的状态和行为。
2.可重用性和可维护性：
面向过程：函数可以被多个地方调用，但数据管理较为复杂，不易维护。
面向对象：对象可以被多次实例化，且对象内部的状态和行为可以独立于其他对象进行修改，便于维护和扩展。
3.抽象和继承：
面向过程：不支持抽象和继承的概念。
面向对象：支持抽象类和继承，可以创建类的层次结构，提高代码的复用性。
4.多态性：
面向过程：不支持多态性。
面向对象：支持多态性，可以在运行时决定调用哪个方法。
通过上述代码示例和说明，可以看出面向过程和面向对象在结构、数据管理、代码复用性等方面存在显著差异。
'''