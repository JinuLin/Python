# 微实例5.6.1科赫曲线绘制
"""
正整数n代表科赫曲线的阶数，表示生成科赫曲线过程的操作次数。
科赫曲线初始化阶数为0，表示一个长度为L的直线。
对于直线L，将其等分为三段，中间一段用边长为L/3的等边三角形的两个边替代，得到1阶科赫曲线，它包含四条线段。
进一步对每条线段重复同样的操作后得到2阶科赫曲线。继续重复同样的操作n次可以得到n阶科赫曲线。
"""
import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.setup(800, 400)
    turtle.speed(0)  # 控制绘制速度
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600, 3)  # 0阶科赫曲线长度，阶数
    turtle.hideturtle()


main()
