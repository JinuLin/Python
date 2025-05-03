# 微实例8.2.2PIL库Image类的解析
from PIL import Image

"""
在PIL中，任何一个图像文件都可以用Image对象表示Image类的图像读取和创建方法。
Image.open(filename)：根据参数加载图像文件
Image.new(mode, size, color)：根据给定参数创建一个新的图像
Image.open(StringIO.StringIO(buffer))：从字符串中获取图像
Image.frombytes(mode, size, data)：根据像素点data创建图像
Image.verify()：对图像文件完整性进行检查，返回异常
"""

"""
要加载一个图像文件，最简单的形式如下，之后所有操作对im起作用
"""
im = Image.open("birdnest.jpg")
"""
Image类有4个处理图片的常用属性：
Image.format：标识图像格式或来源，如果图像不是从文件读取，值是None
Image.mode：图像的色彩模式，"L"灰度图像、"RGB"真彩色图像、"CMYK"出版图像
Image.size：图像宽度和高度，单位是像素（px），返回值是二元元组（tuple）
Image.palette：调色板属性，返回一个ImagePalette类型
"""
print(im.format, im.size, im.mode)
"""
Image还能读取序列的图像文件，包括GIF、FLI、FLC、TIFF等格式文件
Image类的序列图像操作方法：
Image.seek(frame)：跳转并返回图像中的指定帧
Image.tell()：返回当前帧的序号
"""
"""
GIF文件图像提取
通过seek()和tell()方法，可以遍历GIF文件，依次保存每一帧图片
"""

im = Image.open('pybit.gif')  # 读入一个GIF文件
try:
    im.save('picframe{:02d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell() + 1)
        im.save('picframe{:02d}.png'.format(im.tell()))
except EOFError:
    print("处理结束")

"""
Image.save(filename, format) 将图像保存为filename文件名，format是图片格式
Image.convert(mode) 使用不同的参数，转换图像为新的模式
Image.thumbnail(size) 创建图像的缩略图，size是缩略图尺寸的二元元组
"""
"""
save()有两个参数：
filename：保存文件名
format：保存文件格式，默认为原格式
如果调用save()时没有指定保存格式，则保存文件格式为原格式
搭配open()和save()，可以实现格式转换
"""
im = Image.open("birdnest.jpg")
im.save("thumbnail.png")
im.thumbnail((128, 128))
im.save("birdnestTN.jpg", "JPEG")

"""
Image类可以缩放和旋转图像，其中，rotate()方法以逆时针旋转的角度值作为参数来旋转图像。
Image.resize(size)：按size大小调整图像，生成副本
Image.rotate(angle)：按angle角度旋转图像，生成副本
"""
"""
Image类能够对每个像素点或者一幅RGB图像的每个通道单独进行操作，
split()方法能够将RGB图像各颜色通道提取出来，
merge()方法能够将各独立通道再合成一幅新的图像。
Image.point(func)：根据函数func功能对每个元素进行运算，返回图像副本
Image.split()：提取RGB图像的每个颜色通道，返回图像副本
Image.merge(mode，bands)：合并通道 ，采用mode色彩，bands是新色的色彩通道
Image.blend(im1,im2,alpha)：将两幅图片im1和im2按照如下公式插值后生成新的图像：im1 * (1.0-alpha) + im2 * alpha
"""
"""
图像的颜色交换
"""
im = Image.open("birdnest.jpg")
r, g, b = im.split()
om = Image.merge("RGB", (b, g, r))
om.save('birdnestBGR.jpg')

"""
操作图像的每个像素点需要通过函数实现，采用lambda函数和point()方法搭配使用
"""
im = Image.open('birdnest.jpg')  # 打开鸟巢文件
r, g, b = im.split()  # 获得RGB通道数据
new_g = g.point(lambda i: i * 0.9)  # 将G通道颜色值变为原来的0.9倍
newb = b.point(lambda i: i < 100)  # 选择B通道值低于100的像素点
om = Image.merge(im.mode, (r, new_g, newb))  # 将3个通道合形成新图像
om.save('birdnestMerge.jpg')  # 输出图片
