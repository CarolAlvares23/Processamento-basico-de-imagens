import cv2
import numpy as np

image = cv2.imread('images/ajuste_bilho7.jpg')

brilho = 50
imagem_ajustada = np.clip(image.astype(np.int16) + brilho, 0, 255).astype(np.uint8)


cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem com Ajuste de Brilho', imagem_ajustada)
cv2.imwrite('images/ajuste_bilho7_imwrite.jpg', imagem_ajustada)
cv2.waitKey(0)
cv2.destroyAllWindows()
