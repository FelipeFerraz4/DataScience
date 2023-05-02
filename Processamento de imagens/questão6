import cv2
from matplotlib import pyplot as plt

def showImage(image, title, size, mincolor=0, maxcolor=255):
  fig, axis = plt.subplots(figsize = size)

  axis.imshow(image, cmap='gray', vmin=mincolor, vmax=maxcolor)
  axis.set_title(title, fontdict = {'fontsize': 22, 'fontweight': 'medium'})
  plt.show()

image1 = cv2.imread("drive/MyDrive/fotos/mulherSmall.jpg", 0)
image2 = cv2.imread("drive/MyDrive/fotos/logo/LogoWhite.png", 0)
showImage(image1, "mulher", (7, 7))
showImage(image2, "logo", (7, 7))

limiar, image1B = cv2.threshold(image1, 190, 255, cv2.THRESH_BINARY)
showImage(image1B, "mulher", (7, 7))
limiar, image2B = cv2.threshold(image2, 170, 255, cv2.THRESH_BINARY)
showImage(image2B, "logo", (7, 7))

image1Not = cv2.bitwise_not(image1B)
showImage(image1Not, "mulher com a cor invetida", (7, 7))

image1B = cv2.resize(image1B, (500, 500), interpolation = cv2.INTER_LINEAR)
#image2B = cv2.resize(image2B, (500, 500), interpolation = cv2.INTER_LINEAR)
showImage(image1B, "mulher", (7, 7))
imageOr = cv2.bitwise_or(image1B, image2B)
showImage(imageOr, "imagem OR", (7, 7))

image1B = cv2.resize(image1B, (500, 500), interpolation = cv2.INTER_LINEAR)
#image2B = cv2.resize(image2B, (500, 500), interpolation = cv2.INTER_LINEAR)
showImage(image1B, "mulher", (7, 7))
image = cv2.bitwise_and(image1B, image2B)
showImage(image, "imagem AND", (7, 7))

image1B = cv2.resize(image1B, (500, 500), interpolation = cv2.INTER_LINEAR)
#image2B = cv2.resize(image2B, (500, 500), interpolation = cv2.INTER_LINEAR)
showImage(image1B, "mulher", (7, 7))
image = cv2.bitwise_xor(image1B, image2B)
showImage(image, "imagem XOR", (7, 7))

image1B = cv2.resize(image1B, (500, 500), interpolation = cv2.INTER_LINEAR)
#image2B = cv2.resize(image2B, (500, 500), interpolation = cv2.INTER_LINEAR)
showImage(image1B, "mulher", (7, 7))
image = cv2.addWeighted(image1B,0.8, image2B, 0.2,0)
showImage(image, "imagem adição-media", (7, 7))

image1B = cv2.resize(image1B, (500, 500), interpolation = cv2.INTER_LINEAR)
#image2B = cv2.resize(image2B, (500, 500), interpolation = cv2.INTER_LINEAR)
showImage(image1B, "mulher", (7, 7))
image = cv2.subtract(image1B,image2B)
showImage(image, "imagem subtração", (7, 7))

image1B = cv2.resize(image1B, (500, 500), interpolation = cv2.INTER_LINEAR)
#image2B = cv2.resize(image2B, (500, 500), interpolation = cv2.INTER_LINEAR)
showImage(image1B, "mulher", (7, 7))
image = cv2.multiply(image1B,image2B)
showImage(image, "imagem multiplicação", (7, 7))

image1B = cv2.resize(image1B, (500, 500), interpolation = cv2.INTER_LINEAR)
#image2B = cv2.resize(image2B, (500, 500), interpolation = cv2.INTER_LINEAR)
showImage(image1B, "mulher", (7, 7))
image = cv2.divide(image2B,image1B)
showImage(image, "imagem divisão", (7, 7))
