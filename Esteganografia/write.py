import cv2
import numpy as np

print("Insira o nome da imagem: ")
imagem = input()

nameImg = imagem.split(".")

if(nameImg[1] == "ppm"):
    tipo = 1
else:
    tipo = -1

#carregou a imagem
img = cv2.imread("./image/" + nameImg[0] + "." + nameImg[1], tipo)

#Tamnho da imagem
x = img.shape[0]
y = img.shape[1]

yAux = 0
xAux = 0

#Menssagem
print("Insira a menssagem que deseja gravar na imagem: ")
msg = input()
msg = msg + "/"
#Mascara
masc = 1
masc = masc << 7
mascAux = 1

aux = 0
#Converte o char para binario
#print(bin(ord(msg[0])))

#Executa enquanto tiver menssagem
for j in range(len(msg)):
    byte = ord(msg[j])
    #Lê o caracter bit a bit e grava em um byte da imagem, no bit menos significativo
    for i in range(8):
        #Pega um bit da letra
        bit = byte & masc
        #Gambiarra para para pegar o bit impar e não o numero par
        if(bit % 2 == 0 and bit != 0):
            bit = bit +1
        #se o bit par verifica o bit menos significativo da imagem
        if((bit % 2) == 0):
            #Pega o bit menos significativo da imagem
            if(nameImg[1] == 'ppm'):
                byteImg = img.item(xAux,yAux, aux) & mascAux
            elif(nameImg[1] == 'pgm'):
                byteImg = img.item(xAux,yAux) & mascAux
            #Compara o bit da imagem, se for impar, soma um, se não, não faz nada
            if((byteImg % 2) != 0):
                if(nameImg[1] == 'ppm'):
                    img[xAux,yAux, aux] += 1
                else:
                    img[xAux,yAux] += 1
        #Se o bit for impar, compara com o bit da imagem
        elif((bit % 2) != 0):
            #print("Bit é impar")
            if(nameImg[1] == 'ppm'):
                byteImg = img.item(xAux,yAux, aux) & mascAux
            else:
                byteImg = img.item(xAux,yAux) & mascAux
            #Se o bit da imagem dor par, soma um, se não não faz nada
            if((byteImg % 2) == 0):
                if(nameImg[1] == 'ppm'):
                    img[xAux,yAux, aux] += 1
                else:
                    img[xAux,yAux] += 1        
        if(nameImg[1] == 'ppm'):
            if(aux == 2): 
                aux = 0
                #pega o byte seguinte
                yAux += 1
            else:
                aux += 1
        else:
            yAux += 1
        #Anda uma casa do byte para a direita
        masc = masc >> 1
        
        #condição para mudar o x
        if(yAux == y):
            xAux += 1
            yAux = 0
    #reseta a mascara
    masc = 1
    masc = masc << 7
cv2.imwrite("./image/out." + nameImg[1], img)
print("Mensagem gravada com sucesso na imagem!")