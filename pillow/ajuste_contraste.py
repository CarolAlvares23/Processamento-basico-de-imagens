import cv2

image = cv2.imread('images/ajuste_contraste8.jpg')
alpha = 1.5  
beta = 0    


imagem_ajustada = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem com Ajuste de Contraste', imagem_ajustada)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('images/ajuste_contraste8.jpg_imwrite', imagem_ajustada)
