import cv2
from matplotlib import pyplot as plt
"""
Mostrar a uma imagem
"""
obj_img = cv2.imread("../fotos/senhor.jpg")
plt.imshow(obj_img)
plt.show()
