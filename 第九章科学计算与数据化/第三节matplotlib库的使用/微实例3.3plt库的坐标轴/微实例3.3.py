# 微实例9.3.3plt库的坐标轴
import matplotlib.pyplot as plt

"""
plt库有两个坐标体系：图像坐标和数据坐标。
图像坐标将图像所在区域左下角视为原点，将x方向和y方向长度设定为1。
整体绘图区域有一个图像坐标，每个axes()和subplot()函数产生的子图也有属于自己的图像坐标。
axes()函数参数rect 指当前产生的子区域相对于整个绘图区域的图像坐标。
数据坐标以当前绘图区域的坐标轴为参考，显示每个数据点的相对位置，这与坐标系里面标记数据点一致。
"""
"""
plt.axis('v','off','equal','scaled','tight','image') 获取设置轴属性的快捷方法
plt.xlim(xmin,xmax) 设置当前x轴取值范围
plt.ylim(ymin,ymax) 设置当前y轴取值范围
plt.xscale() 设置x轴缩放
plt.yscale() 设置y轴缩放
plt.autoscale() 自动缩放轴视图的数据
plt.thetagrids(angles,labels,fimnt,frac) 设置极坐标网格theta的位置
plt.grid(on/off) 打开或者关闭坐标网格
"""
plt.plot([1, 2, 4], [1, 2, 3])
print(plt.axis())
print(plt.axis((0, 5, 0, 5)))
