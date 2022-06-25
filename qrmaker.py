#! /usr/bin/env python3

# Resources:
# https://pypi.org/project/qrcode/
# https://www.thepythoncode.com/article/generate-read-qr-code-python
# Freecodecamp: https://www.freecodecamp.org/news/python-projects-for-beginners/#qr-code-encoder-decoder-python-project
# https://www.youtube.com/watch?v=SqvVm3QiQVk&t=3192s

import qrcode

url = input("What is your URL?" )
version = int(input("What version of the code would you like? "))
box_size = int(input("What would you like your box size to be? "))
border = int(input("What would you like your boarder size to be? "))
fill_color = input("What would you like your fill color to be? ").lower()
back_color = input("What would you like your back color to be? ").lower()
file_name = input("What would you like your file to be named? ")
file_name = file_name + ".png"
# Options for the qrcode

qcode = qrcode.QRCode(version = version, box_size = box_size, border = border)
# Look of qrcode
qcode.add_data(url)
# Adding data to qrcode
qcode.make(fit=True)
# Make the alterations fit

img = qcode.make_image(fill_color = fill_color, back_color = back_color)
# The colors of the qrcode

img.save(f"/home/shadoughie/Pictures/{file_name}")
# Make sure this file isn't called qrcode.py
# For some reason this will return an error
