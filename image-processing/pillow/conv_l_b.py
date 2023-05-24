from PIL import Image

img = Image.open("images/cc_tc_pb3.jpg")

gray_img = img.convert("L")
pixels = gray_img.load()
threshold = 128

for i in range(img.width):
    for j in range(img.height):
        gray_value = pixels[i, j]
        bin_value = 255 if gray_value >= threshold else 0
        pixels[i, j] = bin_value

gray_img.save("images/cc_tc_pb3_gray.jpg")
