"""
Mostrar uma imagem em escala de cinza
"""
import cv2
from matplotlib import pyplot as plt

obj_img = cv2.imread("../fotos/pessoas.jpg", 0)
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
plt.imshow(obj_img)
plt.show()