# 定义三角形类Triangle
class Triangle:
    def __init__(self, a, b, c):
         self.__a = a
         self.__b = b
         self.__c = c

    # 修改私有属性值
    def set_lens(self, new_a, new_b, new_c):
        if new_a > 0 and new_b > 0 and new_c > 0:
            if new_a+new_b > new_c and new_a+new_c > new_b and new_b+new_c > new_a:
                self.__a = new_a
                self.__b = new_b
                self.__c = new_c
            else:
                print("！！！您输入的是非三角形！！！")
        else:
            print("！！！请正确输入边长！！！")

    # 获取私有属性值
    def get_lens(self):
        return [self.__a, self.__b, self.__c]

# 创建对象
t = Triangle(3, 4, 5)
x = eval(input("请输入第一条边长："))
y = eval(input("请输入第二条边长："))
z = eval(input("请输入第三条边长："))
t.set_lens(x, y, z)
print("三角形的三条边长为：")
for i in t.get_lens():
    print(i, end="   ")
print()
