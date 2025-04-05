# 微实例5.4.1基本数码管绘制
import datetime
import turtle


def drawLine(draw):  # 绘制单段数码管
    # 根据传入的参数draw，如果为True则落笔，否则不落笔
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    # 前进40个单位长度
    turtle.fd(40)
    # 右转90度
    turtle.right(90)


def drawDigit(d):  # 根据数字绘制七段数码管
    # 根据传入的参数d，绘制对应的七段数码管
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):  # 获得要输出的数字
    # 将传入的日期字符串转换为对应的数字，并依次绘制
    for i in date:
        drawDigit(eval(i))  # 注意: 通过eval()函数将数字变为整数


def main():
    # 初始化画布
    turtle.setup(800, 350, 200, 200)
    # 移动到画布中央
    turtle.penup()
    turtle.fd(-300)
    # 设置画笔宽度为5
    turtle.pensize(5)
    # 调用drawDate函数绘制日期
    drawDate(datetime.datetime.now().strftime('%Y%m%d'))
    # 隐藏海龟图标
    turtle.hideturtle()


# 运行主函数
main()
