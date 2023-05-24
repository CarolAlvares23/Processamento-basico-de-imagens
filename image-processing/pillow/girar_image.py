from PIL import Image

img = Image.open('images/girar_90_9.jpg')

img_rotated = img.rotate(-90)

img_rotated.save('images/girar_90_9_rotated.jpg')
