# 1.8太阳花的绘制
from turtle import *

color('red', 'yellow')  # 分别定义填充颜色
begin_fill()
while True:
    forward(200)
    left(170)
    # noinspection PyTypeChecker
    if abs(pos()) < 1:
        break
end_fill()
done()  # 表示绘画结束，停止在窗口，由用户自行关闭
