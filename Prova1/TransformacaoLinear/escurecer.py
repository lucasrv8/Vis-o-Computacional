import cv2

def transformacaoLinear(l1, l2, k1 ,k2 ,valor):
	if valor < l1:
		return k1

	elif l1<= valor & valor < l2:
		return (((k2 - k1)/(l2 - l1))*(valor - l1)) + k1

	elif valor >= l2:
		return k2


img = cv2.imread("Image/prova-01.ppm")
imgTam = img.shape
x = imgTam[1]
y = imgTam[0]


for y in range(y):
	for x in range(x):
		img[y,x,0] = transformacaoLinear(20,100,20,100,img[y,x,0])
		img[y,x,1] = transformacaoLinear(20,100,20,100,img[y,x,1])
		img[y,x,2] = transformacaoLinear(20,100,20,100,img[y,x,2])
			
		

cv2.imshow('Imagem escurecida', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

