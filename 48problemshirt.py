# Run like python shirt.py before1.jpg after1.jpg

import sys
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    if not sys.argv[1].endswith(".jpg"):
        sys.exit(f"Invalid output")
    elif not sys.argv[2].endswith(".jpg"):
        sys.exit(f"Input and output have different extensions")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")

images = []

shirt_img_path = "shirt.png"
face_img_path = sys.argv[1]
output_image_path = sys.argv[2]

with Image.open(face_img_path) as face_img:
    with Image.open(shirt_img_path) as shirt_img:
        # Get the size (width and height) of the shirt image
        shirt_width, shirt_height = shirt_img.size

        # Resize the face image to match the size of the shirt image
        resized_face_img = ImageOps.fit(face_img, (shirt_width, shirt_height))

        # Create a new image with RGBA mode and paste the face image onto it
        new_img = Image.new("RGBA", (shirt_width, shirt_height))
        new_img.paste(resized_face_img, (0, 0))

        # Paste the resized shirt image (shirt.png) on top of the face image
        new_img.paste(shirt_img, (0, 0), shirt_img)

        # Save the resulting image as JPEG (convert to RGB mode)
        new_img.convert("RGB").save(output_image_path)


