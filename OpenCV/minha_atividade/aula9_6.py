'''
Nessa aula criaremos algumas funções para que possamos manipular umas imagens a partir de alguns conceitos básicos
1. Translation(translação): além de ser o movimento que a terra realiza entorno do sol, é também o ato de movimentar um objeto de um ponto a outro
2. Rotation: rotaciona/gira a imagem
3. Resize: redimensiona a imagem
4. Flipping: inverte a imagem, um exemplo clássica são as câmeras de selfie de aparelhos celulares
5. Cropping: o ato de cortar as imagens a partir de coordenadas

Nessa aula utilizaremos muito uma função chamada de warpAffine do CV2. Há uma imagem nos assets/didaticas para explicar melhor o conceito da função.
Mas em suma, qualquer transformação linear em uma série de pontos pode ser descrita por uma matriz seguidade um vetor de adição (translação)
Não é necessário decorar, é apenas um contexto algébrico. Para mais referêncais veja:
https://docs.opencv.org/3.4/d4/d61/tutorial_warp_affine.html
'''

import cv2
import numpy as np

img = cv2.imread('../assets/fotos/park.jpg')
cv2.imshow('Park', img)

# Definições de funções
def translate(img, x, y ):
    '''
    -x Esquerda
    -y Acima
     x Direita
     y Abaixo
    '''
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])

    #coletando as dimensões da nossa imagem
    dimensions = (img.shape[1], img.shape[0])
    #retornar a função warpAfrine
    return cv2.warpAffine(img, translation_matrix, dimensions)

#img_tr = translate(img, 100, 250)
#cv2.imshow('transladado', img_tr)

def rotate(img, angle, rotation_point=None):
    height, width = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width//2, height//2)

    # get matriz de rotação 2d (ponto_de_rotação, angulo, escala)
    rotation_matrix = cv2.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotation_matrix, dimensions)

#rotacionada = rotate(img, -45)
#cv2.imshow('Imagem rotacionada', rotacionada)

#Flipping: Inverte um array 2D
#flip = cv2.flip(img, 1) #horizontal
#flip = cv2.flip(img, 0) #vertical
#flip = cv2.flip(img, -1) #vertical e horizontal

#cv2.imshow('Flipada', flip)


# Resizing e Cropping: recapitulação
#resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
#cv2.imshow('Reize', resized)

# Croping: o ato de cortar as imagens a partir de coordenadas
cropped = img[100:400, 400:600]
cv2.imshow('Cropped', cropped)



cv2.waitKey(0)
cv2.destroyAllWindows()