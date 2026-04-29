import numpy as np
from skimage.transform import rescale
import scipy
import scipy.ndimage
import cv2
import os

FILENAME = 'teste_text.png'
PATH = os.path.join('assets', FILENAME)
img = cv2.imread(PATH)
cv2.imshow('original_image', img)

b_scaled = rescale(img[:,:,0], 0.25)
g_scaled = rescale(img[:,:,1], 0.25)
r_scaled = rescale(img[:,:,2], 0.25)
img_scaled = np.stack([b_scaled, g_scaled, r_scaled], axis=2)

# Box Blur
box_blur = (1 / 9) * np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]])
# Gaussian Blur 3x3
gaussian_3 = (1 / 16) * np.array([[1, 2, 1],
                                  [2, 4, 2],
                                  [1, 2, 1]])
# Gaussian Blur 5x5
gaussian_5 = (1 / 256) * np.array([[1, 4, 6, 4, 1],
                                   [4, 16, 24, 16, 4],
                                   [6, 24, 36, 24, 6],
                                   [4, 16, 24, 16, 4],
                                   [1, 4, 6, 4, 1]])

kernels = [box_blur, gaussian_3, gaussian_5]
kernel_name = ['Box Blur', '3x3 Gaussian Blur', '5x5 Gaussian Blur']

'''
O código entra em um loop, onde itera pelos kernels definidos e seus nomes correspondentes.
Para cada kernel, ele executa convolução usando scipy.ndimage.convolve. 
A função np.atleast_3d é usada para garantir que o kernel tenha o formato apropriado 
para convolução com uma imagem de 3 canais. Torna o kernel tridimensional, 
combinando com a profundidade da imagem.
O parâmetro mode='nearest' em convolve especifica que a convolução deve usar o modo 
de borda mais próximo, o que significa que o tamanho da imagem de saída corresponde 
ao tamanho de entrada.
'''

for kernel, name in zip(kernels, kernel_name):
    conv_im1 = scipy.ndimage.convolve(img, np.atleast_3d(kernel), mode='nearest')
    cv2.imshow(name, conv_im1)

cv2.waitKey(0)