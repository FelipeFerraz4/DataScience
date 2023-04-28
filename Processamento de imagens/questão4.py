import cv2
from matplotlib import pyplot as plt

def showImage(image):
  plt.imshow(image)
  plt.show()
  
  
image = cv2.imread('drive/MyDrive/fotos/mulherSmall.jpg')

image1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
showImage(image1)

image2 = image1[90:440, 310:480]
showImage(image2)

image1[90:440, 0:170] = image2
showImage(image1)

image1[90:440, 670-170:670] = image2
showImage(image1)
