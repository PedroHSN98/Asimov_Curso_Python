import cv2
import numpy as np

#1Processe padrao/inicia
img = cv2.imread('../assets/fotos/cats.jpg')
cv2.imshow('Cats', img)

#Desenhando um canva branco do mesmo tamanho que a imagem de trabalho
blank = np.zeros(img.shape, dtype='uint8')
#cv2.imshow('Blank', blank)

#transferindo-a para cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray', gray)



#2. Detecção de Contornos

#a. Borrar a imagem com o Gaussian Blur
blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
#cv2.imshow('Blur', blur)

#b. Função de Canny
canny = cv2.Canny(blur, 125, 175)
#cv2.imshow('Canny', canny)
"""
A novidade dessa aula começa aqui:
Para detectar os contornos de uma imagem, é recomendado até pela própria biblioteca:
"For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection."

cv2.findContours(imagem, modo_deteccao, metodo_aproximacao_contorno)

Modo de Detecção:
Recomendo a utilização de cv2.RETR_LIST, é o recomendado pela documentação

Métodos de Aproximação de Contorno:
Os contornos são os limites de uma forma com a mesma intensidade na imagem. 
Ele armazena as coordenadas (x,y) do limite de uma forma. Mas ele armazena todas as coordenadas? Isso é especificado por este método de aproximação de contorno.
cv.CHAIN_APPROX_NONE: salva absolutamente todos os pontos de contorno, custoso, imagina se tivessemos uma linha apenas, precisamos de todos os pontos ou apenas seus dois extremos?
cv.CHAIN_APPROX_SIMPLE: Ele remove todos os pontos redundantes e comprime o contorno, economizando memória.
Há um exemplo nos assets/didaticas que mostra duas imagens, na primeira precisamos de 734 pontos para detectar o contorno, na segunda apenas 4, somente variando os métodos
"""

contornos, hierarquia = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'Numeros de contornos encontrados: {len(contornos)}')

cv2.drawContours(blank, contornos, -1, (0, 0, 255), 1)
cv2.imshow('Contornos Desenhados', blank )


cv2.waitKey(0)