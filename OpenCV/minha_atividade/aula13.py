import cv2
import numpy as np 

img = cv2.imread('../assets/fotos/cats.jpg')
cv2.imshow('AsimoCats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
#cv2.imshow('Blank', blank)

#Criar as formas
circle = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
dectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
#cv2.imshow('Circle', circle)
#cv2.imshow('Dectangle', dectangle)

#Criando mascaras diferentes
recorte1 = cv2.bitwise_and(circle, dectangle)
recorte2 = cv2.bitwise_or(circle, dectangle)
recorte3 = cv2.bitwise_not(circle)

cv2.imshow('Recorte', recorte1)
cv2.imshow('Recorte', recorte2)
cv2.imshow('Recorte', recorte3)

#Mostrando as mascaras
mask1 = cv2.bitwise_and(img, img, mask=recorte1)
mask2 = cv2.bitwise_and(img, img, mask=recorte2)
mask3 = cv2.bitwise_and(img, img, mask=recorte3)

cv2.imshow('Mask1', mask1)
cv2.imshow('Mask2', mask2)
cv2.imshow('Mask3', mask3)

cv2.waitKey(0)