"""
fazer uma imagem da bandeira japonesa
"""
import numpy as np
from matplotlib import pyplot as plt


def bandjaponesa(height):
    """
    -> cria uma imagem da bandeira japonesa
    :param height: altura da imagem
    :return: uma imagem da bandeira japonesa
    """
    width = (3*height)//2
    raio = (3*height)//10
    centro = (width//2, height//2)
    red = (188, 0, 45)
    white = (255, 255, 255)
    image = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(0, height):
        for x in range(0, width):

            formula = ((x - centro[0])**2) + ((y - centro[1])**2)

            if formula <= raio**2:
                cor = red
            else:
                cor = white
            image.itemset((y, x, 0), cor[0])
            image.itemset((y, x, 1), cor[1])
            image.itemset((y, x, 2), cor[2])

    return image

# maim program
bandeira = bandjaponesa(400)
plt.imshow(bandeira)
plt.show()
