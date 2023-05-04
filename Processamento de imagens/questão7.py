import cv2
from matplotlib import pyplot as plt
import numpy as np

def showImage(image, title):
  fig, axis = plt.subplots()
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  axis.imshow(image)
  axis.set_title(title)
  plt.show()


image = cv2.imread('balao[1].jpg')
height, width, channel = image.shape
showImage(image, "balao")

Rotation = cv2.getRotationMatrix2D(((width-1)/2.0, (height-1)/2.0), 180, 1)
imageR = cv2.warpAffine(image, Rotation, (width, height))
showImage(imageR, "rotation")

Translation = np.float32([[1,0,-200], [0,1,100]])
imageT = cv2.warpAffine(image, Translation, (width, height))
showImage(imageT, 'Translation')

imageS = cv2.resize(image, None, fx = 2, fy = 2, interpolation = cv2.INTER_LINEAR)
showImage(imageS, "Scaling 2x")
imageS = cv2.resize(image,(int((1/2)*width), int((1/2)*height)), interpolation = cv2.INTER_LINEAR)
showImage(imageS, "Scaling 1/2x")
