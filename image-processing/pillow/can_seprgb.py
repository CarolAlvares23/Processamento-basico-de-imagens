import cv2

image = cv2.imread('images/proc_cores_rgb1.jpg')
b, g, r = cv2.split(image)


cv2.imshow('Canal R', r)
cv2.imshow('Canal G', g)
cv2.imshow('Canal B', b)
cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('images/proc_cores_rgb1_canal_r.jpg', r)
cv2.imwrite('images/proc_cores_rgb1_canal_g.jpg', g)
cv2.imwrite('images/proc_cores_rgb1_canal_b.jpg', b)