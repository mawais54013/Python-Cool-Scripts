# first need to import some libraries

import os, sys
import PIL
from PIL import Image

def convertImg():
    value = input("Please enter png image path:")
    im = Image.open(value)
    im.save(r'/Users/<username here>/Desktop/coverted1.jpg')
    print("Completed, please check your desktop folder for the converted image")

print(convertImg())