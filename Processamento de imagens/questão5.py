import cv2
from matplotlib import pyplot as plt

def showImage(image):
  plt.imshow(image)
  plt.show()
  
image = cv2.imread("drive/MyDrive/fotos/balao.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_sobelx = cv2.Sobel(src=image, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3)
image_sobely = cv2.Sobel(src=image, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3)
image_sobelxy = cv2.Sobel(src=image, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=3)
image_sobelxy2 = cv2.addWeighted(image_sobelx, 0.5, image_sobely, 0.5, 0)
showImage(image)
showImage(image_sobelx)
showImage(image_sobely)
showImage(image_sobelxy)
showImage(image_sobelxy2)
