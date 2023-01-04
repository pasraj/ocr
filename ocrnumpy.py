from PIL import Image
from numpy import array
from pytesseract import image_to_string

file = 'sample.jpg'

img = array(Image.open(file))
text = image_to_string(img)
print(text)

