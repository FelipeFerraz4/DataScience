import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

blue = (255, 0, 0)
red = (0, 0, 255)


def showImage(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()


def drawEllipse(image, rotation, start, end, color, thickness):
    # imagem - (centro) - (a e b da elipse) - rotação - angulo de abertura - angulo de fechamento - cor - espessura
    cv.ellipse(image, (250, 250), (200, 50), rotation, start, end, color, thickness)


def drawCircle(img, color):
    # imagem - centro - raio - espessura se -1 ele preenche
    cv.circle(img, (250, 250), 25, red, -1 )


image = np.zeros((500, 500, 3), dtype=np.uint8)

drawEllipse(image, 0, 0, 360, blue, 2)
drawEllipse(image, 45, 0, 360, blue, 2)
drawEllipse(image, 90, 0, 360, blue, 2)
drawEllipse(image, 135, 0, 360, blue, 2)
drawCircle(image, red)

showImage(image)
