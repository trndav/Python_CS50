# https://youtu.be/5QR-dG68eNE?feature=shared&t=1367

from PIL import Image, ImageFilter

image = Image.open('happy_pup.jpg') # Select image

# Basic filters
image_filter = image.filter(ImageFilter.EMBOSS) 
image_filter_blur = image_filter.filter(ImageFilter.GaussianBlur(radius = 3)) 

image_filter_blur.show()
