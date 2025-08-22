# 微实例2.1图像的数组表示
"""
光线照射使立体物出现明暗变化，运用这个原理是空间素描的基本方法，
采用Python程序增加深浅层次变化，
从而使图像轮廓更富立体感、空间感和色泽感，接近人类手绘效果。
"""
from PIL import Image
import numpy as np

im = np.array(Image.open('fcity.jpg'))
print(im.shape, im.dtype)  # 图像是有规则的二维数据，可以用numpy库将图像转换成数组对象
"""
图像转换对应的ndarray类型是3维数据，如(565,812, 3)，
其中，前两维表示图像的长度和宽度，单位是像素，第三维表示每个像素点的RGB值，
每个RGB 值是一个单字节整数。
"""
"""
PIL 库包括图像转换函数，能够改变图像单个像素的表示形式。
使用convert()函数，这是’L’模式，
表示将像素表示从RGB的3字节形式转变为单一数值形式，
这个数值范围在0到255，表示灰度色彩变化。
"""
im = np.array(Image.open('fcity.jpg').convert('L'))
print(im.shape, im.dtype)
# 此时，图像从彩色变为带有灰度的黑白色。
# 转换后，图像的ndarray类型变为二维数据，每个像素点色彩只由一个整数表示。
"""
通过对图像的数组转换，可以利用numpy访问图像上任意像素值，例如，获取访问位于坐标(10, 150)
像素的颜色值或获取图像中最大和最小的像素值。也可以采用切片方式获取指定行或列的元素值，甚至修改这些值。
"""
print(im[10, 150])
print(int(im.max()), int(im.min()))
print(im[10, :])

"""
将图像读入ndarray数组对象后，可以通过任意数学操作来获取相应的图像变换。
以灰度变换为例，分别对灰度变化后的图像进行反变换、区间变化和像素值平方处理。
"""
im0 = np.array(Image.open('fcity.jpg').convert('L'))
im1 = 255 - im0  # 反变换
im2 = (100 / 255) * im0 + 150  # 区间变换
im3 = 255 * (im1 / 255) ** 2  # 像素值平方处理
pill_im = Image.fromarray(np.uint8(im1))  # 分别对im1、im2、im3执行
# pill_im = Image.fromarray(np.uint8(im2))
# pill_im = Image.fromarray(np.uint8(im3))

pill_im.show()
