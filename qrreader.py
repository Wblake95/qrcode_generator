#! /usr/bin/env python3

from pyzbar.pyzbar import decode
from PIL import Image

pth = input("What is the path to the qrcode? ")
img = Image.open(pth)

result = decode(img)

print(result)
