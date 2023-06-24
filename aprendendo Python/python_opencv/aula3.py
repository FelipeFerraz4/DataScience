import numpy as np
import cv2
from matplotlib import pyplot as plt

def showimagemgrid(img, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()


def showmultipleimagegrid(imgsArray, titlearray, x, y):
    if x < 1 or y < 1:
        print('erro, x ou y não podem ser menores que 1')
        return
    elif x == 1 and y == 1:
        showimagemgrid(imgsArray[0], titlearray[0])
    elif x == 1:
        fig, axis = plt.subplots(y)
        fig.suptitle(titlearray)
        axisid = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[axisid].imshow(imgMPLIB)
            axisid += 1
    elif y == 1:
        fig, axis = plt.subplots(1, x)
        fig.suptitle(titlearray)
        axisid = 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[axisid].imshow(imgMPLIB)
            axisid += 1
    else:
        fig, axis = plt.subplots(y, x)
        xid, yid, titleid = 0, 0, 0
        for img in imgsArray:
            imgMPLIB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            axis[yid, xid].set_title(titlearray[titleid])
            axis[yid, xid].imshow(imgMPLIB)
            if len(titlearray[titleid]) == 0:
                axis[yid, xid].axis('off')
            titleid += 1
            xid += 1
            if xid == x:
                xid = 0
                yid += 1
        fig.tight_layout(pad=0.5)
    plt.show()

def plotsiximages():
    imgoriginal = cv2.imread("fotos/mulher.jpg")
    imgreplicate = cv2.copyMakeBorder(imgoriginal, 200, 100, 50, 25, cv2.BORDER_REPLICATE)
    imgreflect = cv2.copyMakeBorder(imgoriginal, 200, 100, 50, 25, cv2.BORDER_REFLECT)
    imgreflect101 = cv2.copyMakeBorder(imgoriginal, 200, 100, 50, 25, cv2.BORDER_REFLECT_101)
    imgwrap = cv2.copyMakeBorder(imgoriginal, 200, 100, 100, 100, cv2.BORDER_WRAP)
    blue = [255, 0, 0]
    imgconstant = cv2.copyMakeBorder(imgoriginal, 200, 100, 100, 100, cv2.BORDER_CONSTANT, value=blue)

    imgsarray = [imgoriginal, imgreplicate, imgreflect, imgreflect101,
                 imgwrap, imgconstant]
    titlearray = ['original', 'borda replicada',
                  'borda de espelho', 'borda espelho 2',
                  'whap', 'constant']
    showmultipleimagegrid(imgsarray, titlearray, 3, 2)


def plotfourimages():
    imgoriginal = cv2.imread("fotos/mulher.jpg")
    imgreplicate = cv2.copyMakeBorder(imgoriginal, 200, 100, 50, 25, cv2.BORDER_REPLICATE)
    imgreflect = cv2.copyMakeBorder(imgoriginal, 200, 100, 50, 25, cv2.BORDER_REFLECT)
    imgreflect101 = cv2.copyMakeBorder(imgoriginal, 200, 100, 50, 25, cv2.BORDER_REFLECT_101)

    imgsarray = [imgoriginal, imgreplicate, imgreflect, imgreflect101]
    titlearray = ['imagem original', 'imagem com borda replicada',
                  'imagem com borda de espelho',
                  'imagem com borda espelho 2']
    showmultipleimagegrid(imgsarray, titlearray, 2, 2)


def plotthreeimage():
    imgoriginal = cv2.imread("fotos/mulher.jpg")
    imgreplicate = cv2.copyMakeBorder(imgoriginal, 200, 100, 50, 25, cv2.BORDER_REPLICATE)
    imgreflect = cv2.copyMakeBorder(imgoriginal, 200, 100, 50, 25, cv2.BORDER_REFLECT)
    imgtransparent = np.ones((imgoriginal.shape[0], imgoriginal.shape[1], 4), dtype=np.uint8) * 255

    imgsarray = [imgoriginal, imgreplicate, imgreflect, imgtransparent]
    titlearray = ['imagem original', 'imagem com borda replicada',
                  'imagem com borda de espelho', '']
    showmultipleimagegrid(imgsarray, titlearray, 2, 2)


def plottwoimagevertical():
    imgoriginal = cv2.imread("fotos/mulher.jpg")
    imgreplicate = cv2.copyMakeBorder(imgoriginal, 200, 100, 50, 25, cv2.BORDER_REPLICATE)

    imgsArray = [imgoriginal, imgreplicate]
    title = 'imagem original e imagem com borda replicada'
    showmultipleimagegrid(imgsArray, title, 1, 2)


def plottwoimagehorizontal():
    imgoriginal = cv2.imread("fotos/mulher.jpg")
    imgreplicate = cv2.copyMakeBorder(imgoriginal, 200, 100, 50, 25, cv2.BORDER_REPLICATE)

    imgsArray = [imgoriginal, imgreplicate]
    title = 'imagem original e imagem com borda replicada'
    showmultipleimagegrid(imgsArray, title, 2, 1)


def main():
    obj_img = cv2.imread("fotos/mulher.jpg")
    # plottwoimagehorizontal()
    # plottwoimagevertical()
    # plotthreeimage()
    # plotfourimages()
    plotsiximages()
if __name__ == "__main__":
    main()
