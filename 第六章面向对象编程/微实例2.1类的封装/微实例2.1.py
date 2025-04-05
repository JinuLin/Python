# 微实例5.2.1类的封装
"""
类的封装：将数据（属性）与操作数据的方法（行为）绑定在类中，
通过访问控制实现内部细节隐藏，
仅暴露必要接口的编程机制。
"""
"""
使用方法：
1.通过访问控制修饰符（下划线规则）限制属性/方法的可见性
2.对需保护的属性提供公共访问方法（getter/setter）进行读写控制
3.在方法内部实现数据有效性校验等业务逻辑
"""
class Cal:
    def __init__(self, color, speed):
        self.color = color
        self.__speed = speed

    def run(self):
        print("{}的小车以{}千米/小时的速度在奔跑".format(self.color, self.__speed))
    # 修改私有属性值
    def set_speed(self, new_speed):
        if 0 < new_speed < 180:
            self.__speed = new_speed
    # 获取私有属性值
    def get_speed(self):
        return self.__speed

mycar = Cal("白色", 100)
mycar.run()
mycar.color = "黄色"
mycar.set_speed(1000) # 调用方法修改私有属性值
mycar.run()
mycar.set_speed(80) # 调用方法修改私有属性值
mycar.run()

"""
单下划线：_方法名：
约定性私有，提示开发者"不推荐外部直接访问"，但语法上仍可被外部访问
双下划线：__方法名：
触发名称修饰（Name Mangling），使属性变为类内私有，外部无法直接访问（实际可通过 _类名__x 访问）
双头双下划线：__方法名__：
特殊方法/属性标识符，用于Python内置方法（如__init__），开发者应避免自定义使用
"""