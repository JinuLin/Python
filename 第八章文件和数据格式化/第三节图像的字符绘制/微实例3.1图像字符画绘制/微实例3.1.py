# 微实例8.3.1图像字符画绘制
from PIL import Image

"""
位图图片是由不同颜色像素点组成的规则分布，如果采
用字符串代替像素，图像就成为了字符画。
"""
# 定义一个字符集，将这个字符集替代图像中的像素点。
ascii_char = list(r'"$%_&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-/+@<>i!;:,\^`.')
"""
定义彩色向灰度的转换公式如下，其中R、G、B分别是像素点的RGB颜色值：
Gray = R * 0.2126 + G * 0.7152 + B * 0.0722
"""


def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256 / len(ascii_char)
    return ascii_char[int(gray // unit)]


def main():
    im = Image.open('pic.jpg')
    width, height = 100, 60
    im = im.resize((width, height))
    txt = ""
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    fo = open("pic_char.txt", "w")
    fo.write(txt)
    fo.close()


main()
