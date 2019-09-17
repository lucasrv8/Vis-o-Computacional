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

#mascara
masc = 1

#messagem
msg = ""
msgAux = 0

#condição para ler a msg
roda = True
aux = 0
while(roda):
    for i in range(8):
        if(nameImg[1] == 'ppm'):
            byte = img[xAux, yAux, aux]
        else:
            byte = img[xAux, yAux]
        bit = byte & masc
        #Verifica se é impar, se for move um bit para esquerda e incrementa 1
        if(bit % 2 != 0):
            msgAux = msgAux << 1
            msgAux += 1
        #se for par par, apenas move o bit para esquerda colocando zero
        else:
            msgAux = msgAux << 1
        if(nameImg[1] == 'ppm'):
            if(aux == 2): 
                aux = 0
                #pega o byte seguinte
                yAux += 1
            else:
                aux += 1
        else:
            yAux += 1
        #condição para incremetar x
        if(yAux == y):
            xAux += 1
            yAux = 0
    #condição de parada        
    if(str(chr(msgAux)) == '/'):
        roda = False
        msgAux = 0
    #Forma a msg
    msg =  msg + str(chr(msgAux))
    msgAux = 0
print("A frase codificada na imagem é: " + msg)
