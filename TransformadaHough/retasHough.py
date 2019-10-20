import cv2
import numpy as np
import math

img = cv2.imread('Image/plano.png')

#Cópia da imagem para poder desenhas as retas sem alterar a imagem original
imgCopy = img.copy()

#Escala de cinza
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Filtro Gaussiano
imgGaussian = cv2.GaussianBlur(imgGray,(3,3),0)

#Filtro de Sobel
imgSobelEixoX = cv2.Sobel(imgGaussian,cv2.CV_8U,1,0,ksize=5)
imgSobelEixoY = cv2.Sobel(imgGaussian,cv2.CV_8U,0,1,ksize=5)
imgSobel = imgSobelEixoX + imgSobelEixoY

#Filtro de Canny
imgCanny = cv2.Canny(img,100,200)

#Detecção das retas
retas = cv2.HoughLines(imgCanny, 1, math.pi/180.0, 100, np.array([]), 0, 0)

#Desenha as retas na cópia da imagem
a,b,c = retas.shape
for i in range(a):
    rho = retas[i][0][0]
    theta = retas[i][0][1]
    a = math.cos(theta)
    b = math.sin(theta)
    x0, y0 = a*rho, b*rho
    pt1 = (int(x0+1000*(-b)), int(y0+1000*(a)))
    pt2 = (int(x0-1000*(-b)), int(y0-1000*(a)))
    # cv2.line(img, pt1, pt2, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.line(imgCopy, pt1, pt2, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("Imagem Original / Retas encontradas", np.hstack([img, imgCopy]))
cv2.waitKey(0)
cv2.destroyAllWindows()
