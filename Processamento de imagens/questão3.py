import cv2
from matplotlib import pyplot as plt
     
def showImage(image):
  plt.imshow(image)
  plt.show()
  

image = cv2.imread('drive/MyDrive/fotos/balao.jpg')
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
imageYUV = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
showImage(imageRGB)
showImage(imageHSV)
showImage(imageYUV)

def RGB_to_HSI(image):
  import numpy as np
  height, width, channel = image.shape
  for y in range(0, height):
    for x in range(0, width):
      blue = image.item(y, x, 0)
      green = image.item(y, x, 1)
      red =  image.item(y, x, 2)

      I = (blue + green + red)/3
      S = 255 - (3*np.min([blue,green,red])/(blue + green + red)) 
      #erro está dividindo por zero
      H = 255 * np.arccos([ (1/2 * ((red - green) + (red - blue)) ) / ( (red - green)**2 + ( (red - blue)*(green - blue) ) )**(1/2) ])
      
      I = int(I)
      S = int(S)
      H = int(H)

      image.itemset((y, x, 0), I)
      image.itemset((y, x, 1), S)
      image.itemset((y, x, 2), H)
  
  return image
  
  
image = cv2.imread('drive/MyDrive/fotos/balao.jpg')
imageHSI = RGB_to_HSI(image)
showImage(imageHSI)
