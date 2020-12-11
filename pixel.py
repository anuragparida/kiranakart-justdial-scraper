import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy

img = numpy.array(Image.open('heatmaps/heatmapG300a25B.png'))
for row in img:
    for pixel in row:
        if pixel[2] == 1 or pixel[2] < 0.1:
            pixel[0] = 0
            pixel[1] = 0
            pixel[2] = 0


img = Image.fromarray(img, 'RGBA')
img.show()
