import cv2

image = cv2.imread('images/filtro_dg6.jpg')

kernel_size = 5
sigma = 0
blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

cv2.imwrite('images/filtro_dg6.jpg_imwrite', blurred)
