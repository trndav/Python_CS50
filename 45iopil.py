# Create gif from files added as command line
import sys
from PIL import Image

images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)  # from pillow library
    images.append(image)
images[0].save(
    "pymadeanimation.gif",
    save_all=True,
    append_images=[images[1]],
    duration=250,
    loop=0,
)