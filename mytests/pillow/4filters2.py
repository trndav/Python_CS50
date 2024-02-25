# https://youtu.be/5QR-dG68eNE?feature=shared&t=1367

from PIL import Image, ImageFilter

# First way open and show image
image = Image.open('happy_pup.jpg') # Select image

# Basic filters
# image_blur = image.filter(ImageFilter.BLUR) # Blur fixed amount
# image_edge = image.filter(ImageFilter.FIND_EDGES)
# image_filter = image.filter(ImageFilter.EMBOSS)
# image_filter = image.filter(ImageFilter.SMOOTH_MORE)

# Rank filters
# image_filter = image.filter(ImageFilter.MinFilter(size = 3))
# image_filter = image.filter(ImageFilter.MedianFilter(size = 6))

# Multiband
# image_filter = image.filter(ImageFilter.BoxBlur(radius = 3)) # Blur
# image_filter = image.filter(ImageFilter.GaussianBlur(radius = 3))
image_filter = image.filter(ImageFilter.UnsharpMask(radius = 32))

image_filter.show()
