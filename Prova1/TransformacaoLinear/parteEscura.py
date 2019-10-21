import cv2

def transformacaoLinear(k1, k2, l1, l2, img, flag):
    for i in range(x):
        for j in range(y):
            if(img[i,j] < l1):
                img[i,j] = img[i,j]
            elif(img[i,j] >= l1 and img[i, j] < l2):
                img[i,j] = 255
            elif(img[i,j] >= l2):
                img[i,j] = 255
            
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
img = cv2.imread("./../Esteganografia/image/prova-01.ppm", 0)
x = img.shape[0]
y = img.shape[1]
transformacaoLinear(0, 255, 128, 255, img, 1)
