"""
Mostrar imagem com as cores RGB em vez da BGR
"""

import cv2
from matplotlib import pyplot as plt

obj_img = plt.imread("../fotos/criancas.jpg")
# obj_img = cv2.imread("../fotos/criancas.jpg")
# obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
plt.imshow(obj_img)
plt.show()
