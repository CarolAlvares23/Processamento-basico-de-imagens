import cv2

# Carrega a imagem
image = cv2.imread('images/ajuste_contraste8.jpg')

# Define os parâmetros de ajuste de contraste
alpha = 1.5  # Fator de multiplicação para aumentar o contraste
beta = 0    # Valor a ser adicionado para ajustar o brilho

# Realiza o ajuste de contraste
imagem_ajustada = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Exibe a imagem original e a imagem ajustada
cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem com Ajuste de Contraste', imagem_ajustada)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas abertas
cv2.destroyAllWindows()
cv2.imwrite('images/ajuste_contraste8.jpg_imwrite', imagem_ajustada)