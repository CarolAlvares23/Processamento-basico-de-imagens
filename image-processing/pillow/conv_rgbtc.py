from PIL import Image

image = Image.open('images/cc_rgb_tc2.jpg')
gray_image = image.convert('L')

gray_image.save('images/cc_rgb_tc2_gray.jpg')