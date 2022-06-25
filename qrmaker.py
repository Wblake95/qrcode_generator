#! /usr/bin/env python3

# Tutorial:
# Freecodecamp: https://www.freecodecamp.org/news/python-projects-for-beginners/#qr-code-encoder-decoder-python-project
# https://www.youtube.com/watch?v=SqvVm3QiQVk&t=3192s
# Resources:
# https://pypi.org/project/qrcode/
# https://www.thepythoncode.com/article/generate-read-qr-code-python

import qrcode

data = input("What is your URL?" )
# Link in qrcode
version = int(input("What version of the code would you like? "))
boxsize = int(input("What would you like your box size to be? "))
border = int(input("What would you like your boarder size to be? "))
fillcolor = input("What would you like your fill color to be? ").lower()
backcolor = input("What would you like your back color to be? ").lower()

qr = qrcode.QRCode(version = version, box_size = boxsize, border = border)
# Look of qrcode
qr.add_data(data)
# Adding data to qrcode
qr.make(fit=True)
# Make the alterations fit

img = qr.make_image(fill_color = fillcolor, back_color = backcolor)
# The colors of the qrcode

img.save("/home/shadoughie/Pictures/qrcode_make_python.png")
# Make sure this file isn't called qrcode.py
# For some reason this will return an error
