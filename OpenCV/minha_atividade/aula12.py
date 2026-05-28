import cv2
import numpy as np

# criar um canva completamente preto
blank = np.zeros([400, 400], dtype='uint8')
cv2.imshow('Blank', blank)

# IMPORTANTE: utilizar funções copy para não ter problema de aterar duas matrizes ao mesmo tempo
retangulo = cv2.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

cv2.imshow('Retangulo', retangulo)
cv2.imshow('Circulo', circle)

# Bitwise AND -> A intersecção das duas imagens (onde ambos são 1 [branco])
bitwise_and = cv2.bitwise_and(retangulo, circle)
cv2.imshow('Bitwise AND', bitwise_and)

# Bitwise OR -> Intersecção onde há qualquer um dos dois objetivos envolvidos
bitwise_or = cv2.bitwise_or(retangulo, circle)
cv2.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR -> Intessecção onde apenas areas onde há UM OU OUTRO
bitwise_xor = cv2.bitwise_xor(retangulo, circle)
cv2.imshow('Bitwise XOR', bitwise_xor)

# Bitwise NOT -> Inverte a imagem, onde é preto vira branco e vice versa
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow('Bitwise NOT', bitwise_not)

cv2.waitKey(0)

