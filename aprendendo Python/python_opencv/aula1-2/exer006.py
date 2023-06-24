"""
Fazer a bandeira da frança
"""
import numpy as np
from matplotlib import pyplot as plt

def bandfrancesa(height):
    """
    -> Cria uma imagem da bandeira francesa
    :param height: altura da imagem
    :return: Uma imagem da bandeira francesa
    """
    width = (3*height)//2
    white = (255, 255, 255)
    red = (239, 65, 53)
    blue = (0, 85, 164)
    image = np.zeros((height, width, 3), dtype=np.uint8)
    intervalo = width//3
    for y in range(0, height):
        for x in range(0, width):
            if x < intervalo:
                cor = blue
            elif x > 2*intervalo:
                cor = red
            else:
                cor = white
            image.itemset((y, x, 0), cor[0])
            image.itemset((y, x, 1), cor[1])
            image.itemset((y, x, 2), cor[2])
    return image

# main program
bandeira = bandfrancesa(400)
plt.imshow(bandeira)
plt.show()
