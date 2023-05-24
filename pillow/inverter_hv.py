from PIL import Image

img = Image.open('images/inverter_hv10.jpg')

img_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
img_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)

img_horizontal.save('images/inverter_hv10_horizontal.jpg')
img_vertical.save('images/inverter_hv10_vertical.jpg')
