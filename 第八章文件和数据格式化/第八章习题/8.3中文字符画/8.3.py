from PIL import Image

unicode_char = list("天地玄黄宇宙洪荒日月盈昃辰宿列张寒来暑往")


def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256 / len(unicode_char)
    return unicode_char[int(gray // unit)]


def main():
    im = Image.open('pic.jpg')
    width, height = 100, 60
    im = im.resize((width, height))
    txt = ""
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    fo = open("pic_char.txt", "w", encoding="utf-8")
    fo.write(txt)
    fo.close()


main()
