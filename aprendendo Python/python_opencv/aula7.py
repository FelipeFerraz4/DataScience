import numpy as np
import cv2
import time
from tqdm import tqdm

ESCAPE_KEY_ASCII = 27


def onChange(value):
    # print("valor alterado", value)
    pass


# imagem carregada e sua cópia
img = cv2.imread("fotos/mulher200.jpg")
copyimg = img.copy()

# cria janela gráfica para inserir a imagem
windowTitle = "Ajuste de Brilho e Contraste"
cv2.namedWindow(windowTitle)

# cria trackbar
cv2.createTrackbar("contraste", windowTitle, 100, 100, onChange)
cv2.createTrackbar("brilho", windowTitle, 0, 200, onChange)

before_contrast = 100
update_contrast = False

before_brightness = 0
update_brightness = False

counter_time = 0

while True:
    current_contrast = cv2.getTrackbarPos("contraste", windowTitle)
    current_brightness = cv2.getTrackbarPos("brilho", windowTitle)

    # valor de contraste do trackbar foi alterado pelo usuário
    if before_contrast != current_contrast:
        update_contrast = True
        counter_time = time.time()
        before_contrast = current_contrast

    # valor de brilho do trackbar foi alterado pelo usuário
    if before_brightness != current_brightness:
        update_brightness = True
        counter_time = time.time()
        before_brightness = current_brightness

    # se tiver passado 1 segundo desde que o usuário mexeu em algum trackbar
    if time.time() - counter_time > 1:
        # se tiver sido marcado que é pra atualizar contraste ou brilho
        if update_contrast == True or update_brightness == True:
            # fazemos uma cópia da imagem original
            '''
            copyimg = img.copy()

            height, width, channels = img.shape

            #para cada informação de cor, de cada pixel, atualizamos o contraste
            for y in tqdm(range(height)):
                for x in range(width):
                    for c in range(channels):
                        newColorValue = copyimg[y][x][c] * (current_contrast / 100) + current_brightness
                        copyimg[y][x][c] = np.clip(newColorValue, 0, 255)
            '''
            copyimg = cv2.convertScaleAbs(img, alpha=current_contrast / 100, beta=current_brightness)

            update_contrast = False
            update_brightness = False

    cv2.imshow(windowTitle, copyimg)

    keyPressed = cv2.waitKey(1) & 0xFF  # cv2.waitKey(1) & 111111
    if keyPressed == ESCAPE_KEY_ASCII:
        break

cv2.destroyAllWindows()