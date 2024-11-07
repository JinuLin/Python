# 1.7五角星的绘制
from turtle import *  # 从turtle库中导入所有函数

fillcolor("red")  # 表示填充红色
begin_fill()  # 表示开始填充
while True:  # 条件为真时进行死循环
    forward(200)
    right(144)
    # noinspection PyTypeChecker
    if abs(pos()) < 1:  # 判断画笔是否回到原点。
        break  # 判断为是，则跳出循环
end_fill()  # 结束填充
done()
