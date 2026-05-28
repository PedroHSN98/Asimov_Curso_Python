import cv2

'''
Thresholding
-Segmentação de imagens
-A partir de imagens em cinza, criamos imagens binárias
-Melhores condições:
    -Ruído baixo
    -Pixels de um mesmo grupo têm intensidades mais próximas entre si do que pixels de outro grupo
    - Luz Homogênea
'''

img = cv2. imread('../assets/fotos/cats.jpg')
cv2.imshow('Original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gatinhos em tom de cinza', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Para os threshs simples, usaremos a função cv2.theshold()
cv2.threshold(image, valor_de_thresh, max_val, metodo_de_thresholding)

Metodo_de_thresholding:
- cv2.THRESH_BINARY -> focamos nesses dois
- cv2.THRESH_BINARY_INV -> focamos nesses dois
- cv2.THRESH_TRUNC
- cv2.THRESH_TOZERO
- cv2.THRESH_TOZERO_INV
'''

# Thresholding simples
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholding simples', thresh)

# Thresholding simples invertido
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV )
cv2.imshow('Thresholding simples', thresh)

'''
Adaptative Thresholding
cv2.adaptiveThreshold(imagem, valor_maximo, metodo_adaptivo, metodo_thresholding, tamanho_da_vizinhança, constante_C)

meetodo_adaptivo:
- cv2.ADAPTIVE_THRESH_MEAN_C
- cv2.ADAPTIVE_THRESH_GAUSSIAN_C
'''
#Thresholding adaptativo
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
cv2.imshow('Thresholding adaptativo', adaptive_thresh)


cv2.waitKey(0)