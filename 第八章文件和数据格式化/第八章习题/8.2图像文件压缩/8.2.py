from PIL import Image
import os
import math


def getsize(path):
    return os.stat(path).st_size


def compress(path):
    size = getsize(path)
    ratio = math.sqrt(10 * 1024 / size)
    im = Image.open(path)
    height = im.height
    width = im.width
    m_height = int(ratio * height)
    m_width = int(ratio * width)
    ph = im.resize((m_width, m_height))

    ph.save('birdnest_timg.jpg', )


compress('birdnest.jpg')
