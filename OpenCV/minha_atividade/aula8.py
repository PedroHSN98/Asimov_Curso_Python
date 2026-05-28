import cv2
import numpy as np

# RGB -> praticamente o padrão
# BGR -> padrão do OpenCV
# CMYK -> representação para impressões no mundo real

img = cv2.imread('../assets/fotos/cat.jpg')

#BGR para graycale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cinza', gray)

# BGR para HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)


# BGR para L*A*B
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('L*a*b', lab)


# BGR para RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)



cv2.waitKey(0)