# 微实例8.2.3图像的过滤和增强
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
"""
PIL库的ImageFilter类和ImageEnhance类提供了过滤图像和增强图像的方法
ImageFilter.BLUR 图像的模糊效果
ImageFilter.CONTOUR 图像的轮廓效果
ImageFilter.DETAIL 图像的细节效果
ImageFilter.EDGE_ENHANCE 图像的边界加强效果
ImageFilter.EDGE_ENHANCE_MORE 图像的阈值边界加强效果
ImageFilter.EMBOSS 图像的浮雕效果
ImageFilter.FIND_EDGES 图像的边界效果
ImageFilter.SMOOTH 图像的平滑效果
ImageFilter.SMOOTH_MORE 图像的阈值平滑效果
ImageFilter.SHARPEN 图像的锐化效果
"""
"""
利用Image类的filter()方法可以使用ImageFilter类：
Image.filter(ImageFilter.fuction)
"""
"""
图像轮廓获取
"""
im = Image.open('birdnest.jpg')
om = im.filter(ImageFilter.CONTOUR)
om.save('birdnestContour.jpg')

"""
ImageEnhance类提供了更高级的图像增强需求，它提供调整色彩度、亮度、对比度、锐化等功能。
ImageEnhance.enhance(factor)：对选择属性的数值增强factor倍
ImageEnhance.Color(im)：调整图像的颜色平衡
ImageEnhance.Contrast(im)：调整图像的对比度
ImageEnhance.Brightness(im)：调整图像的亮度
ImageEnhance.Sharpness(im)：调整图像的锐度
"""
"""
图像的对比度增强
"""
im = Image.open('birdnest.jpg')
om = ImageEnhance.Contrast(im)
om.enhance(20).save('birdnestEnContrast.jpg')
