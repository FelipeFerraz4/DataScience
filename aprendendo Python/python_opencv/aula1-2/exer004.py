"""
Criar uma imagem que tem parte copiada e colaada em outra parte.
"""
import cv2
from matplotlib import pyplot as plt

obj_img = cv2.imread("../fotos/mulher.jpg")
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
hand = obj_img[2270:2270+700, 4400:4400+500]
obj_img[800 : 800+hand.shape[0], 5800:5800+hand.shape[1]] = hand
plt.imshow(obj_img)
plt.show()
