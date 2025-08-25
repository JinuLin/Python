# 微实例9.2.2图像的手绘效果
"""
手绘图像的基本思想是利用像素之间的梯度值（而不是像素本身）重构每个像素值。
为了体现光照效果，设计一个光源，建立光源对各点梯度值的影响函数，进而运算出新的像素值，
从而体现边界点灰度变化，形成手绘效果。
"""
import numpy as np
from PIL import Image

vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
vec_az = np.pi / 4.  # 光源的方位角度，弧度值
depth = 10.  # (0-100)
"""
将光源定义为三个参数：方位角vec_az、俯视角vec_el和深度权值depth。
两个角度的设定和单位向量构成了基础的柱坐标系，体现物体相对于虚拟光源的位置
"""
im = Image.open('fcity.jpg').convert('L')
a = np.asarray(im).astype('float')
grad = np.gradient(a)  # 取图像灰度的梯度值
grad_x, grad_y = grad  # 分别取横纵图像梯度值
grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.
"""
通过np.gradient()函数计算图像梯度值作为新色彩计算的基础。
为了更直观的进行计算，可以把角度对应的柱坐标转化为xyz 立体坐标系。
dx、dy、dz 是像素点在施加模拟光源后在x、y、z 方向上明暗度变化的加权向量
"""
dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x轴的影响
dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y轴的影响
dz = np.sin(vec_el)  # 光源对z轴的影响
"""
A 是梯度幅值，也是梯度大小。各个方向上总梯度除以幅值得到每个像素单元的梯度值。
利用每个单元的梯度值和方向加权向量合成灰度值，clip 函数用预防溢出，并归一化到0‐255 区间。
最后从数组中恢复图像并保存。
"""
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A
a2 = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
a2 = a2.clip(0, 255)
"""
在利用梯度重构图像时，对应不同梯度取0‐255 之间不同的灰度值，
depth的作用就在于调节这个对应关系。
depth较小时，背景区域接近白色，画面显示轮廓描绘；
depth较大时，整体画面灰度值较深，近似于浮雕效果
"""
im2 = Image.fromarray(a2.astype('uint8'))  # 重构图像
im2.save('fcityHandDraw.jpg')
