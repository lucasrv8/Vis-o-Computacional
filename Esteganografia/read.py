import cv2

print("Insira o nome da imagem: ")
imagem = input()

nameImg = imagem.split(".")

if(nameImg[1] == "ppm"):
    tipo = 1
else:
    tipo = 0

#Carrega Imagem
img = cv2.imread("./image/" + nameImg[0] + "." + nameImg[1], tipo)

#Tamanho da imagem
x = img.shape[0]
y = img.shape[1]

xAux = 0
yAux = 0

#Mascara
masc = 1

#Messagem
msg = ""
msgAux = 0

#Condição para ler a menssagem
roda = True
aux = 0
while(roda):
    for i in range(8):
        if(nameImg[1] == 'ppm'):
            byte = img[xAux, yAux, aux]
        else:
            byte = img[xAux, yAux]
        bit = byte & masc
        #Verifica se é impar, se for, move um bit para esquerda e incrementa 1
        if(bit % 2 != 0):
            msgAux = msgAux << 1
            msgAux += 1
        #Se for par, apenas move o bit para esquerda colocando zero
        else:
            msgAux = msgAux << 1
        if(nameImg[1] == 'ppm'):
            if(aux == 2): 
                aux = 0
                #Pega o byte seguinte
                yAux += 1
            else:
                aux += 1
        else:
            yAux += 1
        #Condição para incremetar x
        if(yAux == y):
            xAux += 1
            yAux = 0
    #Condição de parada        
    if(str(chr(msgAux)) == '/'):
        roda = False
        msgAux = 0
    #Forma a menssagem
    msg =  msg + str(chr(msgAux))
    msgAux = 0
print("A frase codificada na imagem é: " + msg)