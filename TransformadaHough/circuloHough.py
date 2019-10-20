import cv2
import numpy as np
import math

img = cv2.imread('Image/bola.jpg')

#Cópia da imagem para poder desenhas as retas sem alterar a imagem original
imgCopy = img.copy()

#Escala de cinza
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Filtro Gaussiano
imgGaussian = cv2.GaussianBlur(imgGray,(11, 11), 1)

#Filtro de Sobel
imgSobelEixoX = cv2.Sobel(imgGaussian,cv2.CV_8U,1,0,ksize=5)
imgSobelEixoY = cv2.Sobel(imgGaussian,cv2.CV_8U,0,1,ksize=5)
imgSobel = imgSobelEixoX + imgSobelEixoY

#Filtro de Canny
imgCanny = cv2.Canny(img,100,200)

#Detecção de Círculos
circles = cv2.HoughCircles(imgGray, cv2.HOUGH_GRADIENT, 1, 20, param1=65, param2=50, minRadius=0, maxRadius=0)
detected_circles = np.uint16(np.around(circles))

#Desenhando os cículos encontrados na cópia da imagem
for (x, y ,r) in detected_circles[0, :]:
    cv2.circle(imgCopy, (x, y), r, (0, 255, 255), 2)
    cv2.circle(imgCopy, (x, y), 2, (0, 0, 255), 2)
    
cv2.imshow("Imagem Original / Círculos encontrados", np.hstack([img, imgCopy]))
cv2.waitKey(0)
cv2.destroyAllWindows()
