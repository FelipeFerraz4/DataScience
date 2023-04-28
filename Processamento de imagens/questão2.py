import cv2
from matplotlib import pyplot as plt

def showImage(image):
  plt.imshow(image)
  plt.show()
  

color_imageBGR = cv2.imread("drive/MyDrive/fotos/balao.jpg")
color_imageRGB = cv2.cvtColor(color_imageBGR, cv2.COLOR_BGR2RGB)
gray_imageBGR = cv2.cvtColor(color_imageBGR, cv2.COLOR_BGR2GRAY)
gray_imageRGB = cv2.cvtColor(gray_imageBGR, cv2.COLOR_BGR2RGB)

showImage(color_imageBGR)
showImage(color_imageRGB)
showImage(gray_imageBGR)
showImage(gray_imageRGB)

def grayscale(image):
  height, width, channel = image.shape
  for y in range(0, height):
    for x in range(0, width):

      blue = image.item(y, x, 0)
      green = image.item(y, x, 1)
      red =  image.item(y, x, 2)

      media = int((blue + green + red)/3)

      image.itemset((y, x, 0), media)
      image.itemset((y, x, 1), media)
      image.itemset((y, x, 2), media)

  return image


image = cv2.imread("drive/MyDrive/fotos/balao.jpg")
gray_imageFunction = grayscale(image)
showImage(gray_imageFunction)

def grayscale2(image):
  height, width, channel = image.shape
  for y in range(0, height):
    for x in range(0, width):

      blue = image.item(y, x, 0)
      green = image.item(y, x, 1)
      red =  image.item(y, x, 2)

      media = int( (red*0.3) + (green*0.59) + (blue*0.11) )

      image.itemset((y, x, 0), media)
      image.itemset((y, x, 1), media)
      image.itemset((y, x, 2), media)

  return image


image = cv2.imread("drive/MyDrive/fotos/mulher.jpg")
gray_imageFunction = grayscale(image)
showImage(gray_imageFunction)
gray_imageFunction2 = grayscale2(image)
showImage(gray_imageFunction2)
