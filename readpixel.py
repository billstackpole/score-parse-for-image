__author__ = 'bill'
import os, sys
from PIL import Image
i = Image.open("/Users/bill/ccdcFriday/Saturday/test_image.jpg")

print i.format, i.size, i.mode
print i.info

pixels = i.load() # this is not a list, nor is it list()'able
width, height = i.size

all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        all_pixels.append(cpixel)

print pixels[135,150]
print pixels[135,200]
print pixels[135,250]
print pixels[135,300]
print pixels[135,350]
print pixels[135,390]
print pixels[135,440]
print pixels[135,490]
print pixels[135,540]
print pixels[135,590]


print pixels[235,150]
print pixels[235,200]
print pixels[235,250]
print pixels[235,300]
print pixels[235,350]
print pixels[235,390]
print pixels[235,440]
print pixels[235,490]
print pixels[235,540]
print pixels[235,590]