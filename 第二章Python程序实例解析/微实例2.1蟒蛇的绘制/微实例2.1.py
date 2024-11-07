# 微实例2.2.1蟒蛇的绘制
import turtle  # 调用turtle（海龟绘图）加as t表示将库名改命名为t，后续用t.(函数名表式)。

# 可以用from turtle import * 表示

turtle.setup(650, 350, 200, 200)  # setup设置窗口大小
"""
setup(
650是窗口宽度（整数表示像素，小数表示窗口宽度与屏幕的比）
350窗口高度（整数表示像素，小数表示窗口高度与屏幕的比）
200是窗口左侧与屏幕左侧的像素距离（如果值为None，窗口位于屏幕水平中央）
200是窗口顶端与屏幕底端的像素距离（如果值为None，窗口位于屏幕垂直中央）
)"""
turtle.penup()  # penup或pu或up，抬起画笔
turtle.fd(-250)  # fd或forward，控制画笔前进方向距离，值为负值时，反方向前进
turtle.pendown()  # pendown或pd或down，落下画笔
turtle.pensize(25)  # pensize或width，设置画笔宽度，无参数时输入时返回当前画笔宽度，None或空，则函数返回当前画笔宽度
turtle.pencolor("purple")  # pencolor或color，设置画笔颜色，为空则为黑色
turtle.seth(-40)  # seth控制前进角度
for i in range(4):  # 用for做遍历循环赋值给i，给函数range
    turtle.circle(40, 80)  # 绘制弧形,circle(radius(弧的半径),extent(圆心角的度数),steps(弧的段数))
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()  # 不让窗口关闭
