import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

blue = (255, 0, 0)
red = (0, 0, 255)
black = (0, 0, 0)

def showImage(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def drawTriangle(img, color, position):
    positionS = [(75, 75), (175, 75), (275, 75),
                 (75, 175), (175, 175), (275, 175),
                 (75, 275), (175, 275), (275, 275)]
    positionM = [(75, 125), (175, 125), (275, 125),
                 (75, 225), (175, 225), (275, 225),
                 (75, 325), (175, 325), (275, 325)]
    positionE = [(125, 125), (225, 125), (325, 125),
                 (125, 225), (225, 225), (325, 225),
                 (125, 325), (225, 325), (325, 325)]

    # vertices do triangulo
    triangle = np.array([[positionS[position], positionM[position], positionE[position]]], np.int32)
    cv.fillPoly(img, triangle, color)


def drawRectangle(img, color, position):
    positionX = [[75, 75], [175, 75], [275, 75],
                 [75, 175], [175, 175], [275, 175],
                 [75, 275], [175, 275], [275, 275]]
    positionY = [[125, 125], [225, 125], [325, 125],
                 [125, 225], [225, 225], [325, 225],
                 [125, 325], [225, 325], [325, 325]]

    # imagem - canto superior esquerdo - canto inferior direito - cor - espessura(se -1 ele preenche a figura)
    cv.rectangle(img, positionX[position], positionY[position], color, -1)

jogoImage = np.zeros((400, 400, 3), dtype=np.uint8)
jogoImage.fill(255)
# imagem - inicio da linha - fim da linha - cor - espessura
cv.line(jogoImage, (50, 150), (350, 150), black, 2)  # horizontal
cv.line(jogoImage, (50, 250), (350, 250), black, 2)  # horizontal
cv.line(jogoImage, (150, 50), (150, 350), black, 2)  # vertical
cv.line(jogoImage, (250, 50), (250, 350), black, 2)  # vertical

drawRectangle(jogoImage, red, 8)
drawTriangle(jogoImage, blue, 0)

showImage(jogoImage)
