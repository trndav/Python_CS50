from PIL import Image

# First way open and show image
image = Image.open('happy_pup.jpg') # Select image
# image.show() # Show image

# # Second way open and show image
# with Image.open("happy_pup.jpg") as image:
#     image.show()

# Create new image
# image_blank = Image.new('RGBA', (500,400)) # model and size. RGBA - A can be transparent
# image_blank.show()

# Saving image
image.save("saved_img.jpg")

# Image information
print(image.size)
print(image.filename)
print(image.format)
print(image.format_description)
