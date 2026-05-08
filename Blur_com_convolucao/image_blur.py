import numpy as np
from skimage.transform import rescale
import scipy
import scipy.ndimage
import cv2
import os


FILENAME = 'teste_img.jpg'
PATH = os.path.join('assets', FILENAME)

img = cv2.imread(PATH)
cv2.imshow('Imagem original', img)
blue = rescale(img[:, :, 0], 0.5)
green = rescale(img[:, :, 1], 0.5)
red = rescale(img[:, :, 2], 0.5)
img_scaled = np.stack([blue, green, red], axis= 2)
cv2.imshow('Imagem rescaled', img_scaled)


cv2.waitKey(0)