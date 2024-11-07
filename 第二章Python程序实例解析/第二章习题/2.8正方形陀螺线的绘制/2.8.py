import turtle

turtle.speed('fastest')  # 加快画笔速度
length = 3  # 正方形边长
angle = 90  # 转向角度
for i in range(100):  # 循环n次，画n个边形
    turtle.forward(length)
    turtle.right(angle)
    length += 2  # 每次增加一定长度，形成螺旋效果
turtle.done()  # 保持绘图窗口显示
