from PIL import Image, ImageColor # Image color to use words instead of RGB

# First way open and show image
image = Image.open('happy_pup.jpg') # Select image
# image.show() # Show image

# Rotate and show image
# image_rotate = image.rotate(60, expand=True, fillcolor=(255,255,255)) # Rotate and expand to fit whole image
image_rotate = image.rotate(60, expand=True, fillcolor= ImageColor.getcolor('blue','RGB'))
# print(ImageColor.getcolor('blue','RGB')) # Get values

# Crop
image_crop = image.crop((0, 0, 500, 400)) # crop left_x, top_y, right_x, bottom_y
# image_crop.show()
# print(image.size)
# print(image_crop.size)

# Flip horizontal / vertical
image_flip_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
image_flip_vertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
image_flip_transpose = image.transpose(Image.Transpose.TRANSPOSE)
# We can use ROTATE_90, ROTATE_180, TRANSPOSE, TRANSVERSE
# image_flip_transpose.show()

# Resize image
image_resize = image.resize((400, 300))  # (Width, Height) - no aspect ratio
scale_factor = 2
new_image_size = (image.size[0] * scale_factor, image.size[1] * scale_factor)
image_resize_ratio = image.resize(new_image_size)
image_resize_ratio.show()