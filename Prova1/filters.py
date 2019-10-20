import cv2
import numpy as np

# file = input("Insira o nome da imagem: ")
img = cv2.imread('Image/prova-01.ppm')

ddepth = cv2.CV_16S
kernel_size = 3

#Escala de cinza
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Filtro Média
imgMedia = cv2.blur(img,(7,7))

#Filtro Laplaciano
auxLaplacian = cv2.Laplacian(imgGray, ddepth, ksize=kernel_size)
imgLaplacian = cv2.convertScaleAbs(auxLaplacian)

#Filtro Gaussiano
imgGaussian = cv2.GaussianBlur(imgGray,(3,3),0)

#Filtro de Canny
imgCanny = cv2.Canny(img,100,200)

#Filtro de Sobel
imgSobelEixoX = cv2.Sobel(imgGaussian,cv2.CV_8U,1,0,ksize=5)
imgSobelEixoY = cv2.Sobel(imgGaussian,cv2.CV_8U,0,1,ksize=5)
imgSobel = imgSobelEixoX + imgSobelEixoY

#Filtro de Prewitt
mascEixoX = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
mascEixoY = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
imgPrewittEixoX = cv2.filter2D(imgGaussian, -1, mascEixoX)
imgPrewittEixoY = cv2.filter2D(imgGaussian, -1, mascEixoY)
imgPrewitt = imgPrewittEixoX + imgPrewittEixoY

#Filtro de Roberts
mascRobertsEixoX = np.array([[0, 0, 0], [0, 1, 0], [0, 0, -1]])
mascRobertsEixoY = np.array([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
robertsEixoX = cv2.filter2D(img, -1, mascRobertsEixoX)
robertsEixoY = cv2.filter2D(img, -1, mascRobertsEixoY)
imgRoberts = robertsEixoX + robertsEixoY

#Exibe os resultados
cv2.imshow("Imagem original", img)
cv2.imshow("Filtros de suavização: Média", imgMedia)
cv2.imshow("Filtros de suavização: Gaussiano", imgGaussian)
cv2.imshow("Filtros de detecção de borda: Laplacian", imgLaplacian)
cv2.imshow("Filtros de detecção de borda: Canny", imgCanny)
cv2.imshow("Filtros de detecção de borda: Sobel", imgSobel)
cv2.imshow("Filtros de detecção de borda: Prewitt", imgPrewitt)
cv2.imshow("Filtros de detecção de borda: Roberts", imgRoberts)

cv2.waitKey(0)
cv2.destroyAllWindows()