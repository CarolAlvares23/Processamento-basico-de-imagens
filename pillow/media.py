import numpy as np
from PIL import Image
from scipy.ndimage import uniform_filter

image = Image.open('images/filtro_media4.jpg')
image_array = np.array(image)

filtered_image_array = uniform_filter(image_array, size=3)
filtered_image = Image.fromarray(filtered_image_array.astype(np.uint8))

filtered_image.save('images/filtro_media4_filterd.jpg')
