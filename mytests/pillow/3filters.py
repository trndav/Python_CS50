# https://youtu.be/5QR-dG68eNE?feature=shared&t=1367

from PIL import Image, ImageEnhance

# First way open and show image
image = Image.open('happy_pup.jpg') # Select image

# Create enhancer
color_enhancer = ImageEnhance.Color(image) # Color intensity
contrast_enhancer = ImageEnhance.Contrast(image) # Contrast
brightness_enhancer = ImageEnhance.Brightness(image)
sharpness_enhancer = ImageEnhance.Sharpness(image)

# Applying enhancer
# enhanced_image = color_enhancer.enhance(0.2) # 0 black/white, 1 default.
# enhanced_image = contrast_enhancer.enhance(0.5)
# enhanced_image = brightness_enhancer.enhance(3) # Brightness
enhanced_image = sharpness_enhancer.enhance(4)
enhanced_image.show()
