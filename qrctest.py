#! /usr/bin/env python3

# Tutorial:
# Freecodecamp: https://www.freecodecamp.org/news/python-projects-for-beginners/#qr-code-encoder-decoder-python-project
# https://www.youtube.com/watch?v=SqvVm3QiQVk&t=3192s
# Resources:
# https://pypi.org/project/qrcode/
# https://www.thepythoncode.com/article/generate-read-qr-code-python

import qrcode

data = "https://www.twitch.tv/thnx4dying1"

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)

qr.make(fit = True)

img = qr.make_image(fill_color = "orange", back_color = "blue")
# Make sure this file isn't called qrcode.py
# For some reason this will return an error

img.save("/home/shadoughie/python_projects/qrcode_make_python.png")

