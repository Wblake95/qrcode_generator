#! /usr/bin/env python3

# Resources:
# https://pypi.org/project/qrcode/
# https://www.thepythoncode.com/article/generate-read-qr-code-python
# Freecodecamp: https://www.freecodecamp.org/news/python-projects-for-beginners/#qr-code-encoder-decoder-python-project
# https://www.youtube.com/watch?v=SqvVm3QiQVk&t=3192s
# https://www.geeksforgeeks.org/python-os-path-expanduser-method/
# https://www.demo2s.com/python/python-sys-platform.html
# https://www.demo2s.com/python/python-os-function-list.html
# https://stackoverflow.com/questions/72757412/cli-that-find-the-pictures-folder-of-the-operating-system/72763503#72763503

import qrcode
import sys
import os
# In order of use

url = input("What is your URL? ")
version = input("\nWhat version of the code would you like?\nValue 1-40 (default = 1, 21x21 matrix): ")
box_size = input("\nWhat would you like your box size to be?\nSize of boxes in pixels (default = 10): ")
border = input("\nWhat would you like your boarder size to be?\nSize of boarder in pixels (default = 4): ")
fill_color = input("\nWhat would you like your fill color to be?\n(default = Black): ").lower()
back_color = input("\nWhat would you like your back color to be?\n(default = White): ").lower()
file_name = input("\nWhat would you like your file to be named?\n(leave out the file type, e.g. .png): ")
file_name = file_name + ".png"
# Options for the qrcode

if version == "":version = 1
version = int(version)
if box_size == "":box_size = 10
box_size = int(box_size)
if border == "":border = 4
border = int(border)
if fill_color == "":fill_color = "black"
if back_color == "":back_color = "white"
if file_name == "": file_name = "file_name"

qcode = qrcode.QRCode(version = version, box_size = box_size, border = border)
# Look of qrcode
qcode.add_data(url)
# Adding data to qrcode
qcode.make(fit=True)
# Make the alterations fit
img = qcode.make_image(fill_color = fill_color, back_color = back_color)
# The colors of the qrcode

if sys.platform.startswith("linux"):
    userpath = os.path.expanduser("~")
    img.save(f"{userpath}/Pictures/{file_name}")
elif sys.platform.startswith("win"):
    userpath = os.path.expanduser("~")
    img.save(f"{userpath}/Pictures/{file_name}")
elif sys.platform.startswith("darwin"):
    userpath = os.path.expanduser("~")
    img.save(f"{userpath}/Pictures/{file_name}")
    #img.save(f"${HOME}/Pictures/{file_name}")
# Check OS type and path to Pictures folder
# Make sure this file isn't called qrcode.py
# For some reason this will return an error
