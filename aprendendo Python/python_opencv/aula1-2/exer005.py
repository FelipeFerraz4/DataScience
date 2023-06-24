"""
Fazer um triangulo.
"""
import numpy as np
from matplotlib import pyplot as plt


def triangulo(size):
    """
    -> Cria um triangulo preto e branco
    :param size: a largura e altura da imagem
    :return: uma imagem de um triangulo preto
    """
    width = height = size
    triangulo_img = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(0, height):
        for x in range(0, width):
            if y < x:
                triangulo_img.itemset((y, x, 0), 255)
                triangulo_img.itemset((y, x, 1), 255)
                triangulo_img.itemset((y, x, 2), 255)

    return triangulo_img

# main program
obj_img = triangulo(400)
plt.imshow(obj_img)
plt.show()
