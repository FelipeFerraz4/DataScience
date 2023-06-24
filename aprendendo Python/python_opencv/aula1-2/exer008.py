"""
Criar uma imagem de um modelo de bandeira brasileira
"""
import numpy as np
from matplotlib import pyplot as plt


def bandbrasileira(height):
    modulo = height // 14
    width = modulo * 20
    raio = int(3.5*modulo)
    centro = (width//2, height//2)
    margem = int(1.7*modulo)
    image = np.zeros((height, width, 3), dtype=np.uint8)
    green = (0, 156, 59)
    yellow = (255, 223, 0)
    blue = (0, 39, 118)
    # white = (255, 255, 255)
    for y in range(0, height):
        for x in range(0, width):
            formulaCircunfencia = (x - centro[0])**2 + (y - centro[1])**2

            if formulaCircunfencia <= raio**2:
                cor = blue
            elif (y > margem and y < (height-margem)) and (x > margem and x < (width-margem)):
                if y <= centro[1] and x <= centro[0] and (centro[1]-y) <= (5.3/8.3)*(x - margem):
                    cor = yellow
                elif y <= centro[1] and x > centro[0] and (centro[1]-y) <= (-5.3/8.3)*(x - centro[0]) + centro[1] - margem:
                    cor = yellow
                elif y > centro[1] and x <= centro[0] and (y - centro[1]) <= (5.3/8.3)*(x - margem):
                    cor = yellow
                elif y > centro[1] and x > centro[0] and (y - centro[1]) <= (-5.3/8.3)*(x - centro[0]) + centro[1] - margem:
                    cor = yellow
                else:
                    cor = green
            else:
                cor = green
            image.itemset((y, x, 0), cor[0])
            image.itemset((y, x, 1), cor[1])
            image.itemset((y, x, 2), cor[2])
    return image


bandeira = bandbrasileira(300)
plt.imshow(bandeira)
plt.show()
