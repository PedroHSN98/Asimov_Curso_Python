import cv2
import numpy as np

img = cv2.imread('../assets/fotos/park.jpg')

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cinza', cinza)

# Metodo Laplaciano
#cv2.Laplacian()
laplacian = cv2.Laplacian(cinza, cv2.CV_64F)
#cv2.imshow('Laplacian', laplacian)
#print(laplacian)

#Calcular o valor absoluto por elemento e converter para uint8 (0 a 255)
laplacian2 = np.uint8(np.absolute(laplacian))
#cv2.imshow('Laplacian 2 refaturado', laplacian2)


#Metodo de Sobel
#cv2.Sobel(imagem, ddepth, dx, dy), onde dx e dy representa a direção da detecção de bordas
x = cv2.Sobel(cinza, cv2.CV_64F, 1, 0)
y = cv2.Sobel(cinza, cv2.CV_64F, 0, 1)

#resultados separados das bordas horizontais e verticais
#cv2.imshow('Sobel X', x)
#cv2.imshow('Sobel Y', y)   


#Combinar x e y em uma bitwise operation
combined_sobel = cv2.bitwise_or(x, y)
cv2.imshow('Sobel combinado', combined_sobel)

#Metodo de Canny
canny = cv2.Canny(cinza, 150, 175)
cv2.imshow('Canny', canny)


cv2.waitKey(0)