#Muito importante quando vamos trabalhar com detecção de bordas, detecção de formas, etc. Pois é necessário trabalhar com os canais de cores separadamente. Por exemplo, se quisermos detectar bordas em uma imagem, podemos usar o canal de cor azul para isso, pois ele pode conter mais informações sobre as bordas do que os outros canais. Além disso, ao trabalhar com os canais de cores separadamente, podemos aplicar diferentes técnicas de processamento de imagem em cada canal, o que pode melhorar a qualidade da imagem final.
import cv2
import numpy as np

img = cv2.imread('../assets/fotos/park.jpg')
cv2.imshow('Fim de semana no parque', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#cv2.imshow('Blank', blank)

# Desintegrando as imagens
b, g, r = cv2.split(img)


# Reintegrando os canais de cores
blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

#cv2.imshow('Blue', blue)
#cv2.imshow('Green', green)
#cv2.imshow('Red', red)

#print(img.shape) ''' Aqui possuem 3 canais, ou seja, 3 dimensões, que seria o azul, verde e vermelho. Nos demais não é demonstrado pois é valor 1, ou seja, não é demonstrado ao lado do valor de dimensão.'''
#print(b.shape)
#print(g.shape)
#print(r.shape)


# Reintegrando as imagens
merged = cv2.merge([b, g, r])
cv2.imshow('Merged', merged)
print(merged.shape)
print(img.shape)

cv2.waitKey(0)