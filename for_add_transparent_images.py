#!/usr/bin/env python3

from PIL import Image
import glob
import subprocess

# use ImageMagic to split gif movie
subprocess.call('convert out/image.gif +adjoin out/out.gif'.split())

gif_list = glob.glob('out/*.gif')
print(gif_list)

gif = gif_list[0]
org = Image.open(gif)
org = org.convert('RGB')

trans = Image.new('RGBA', org.size, (0, 0, 0, 0))

width = org.size[0]
height = org.size[1]

org.close()



for gif in gif_list[1:]:
    print(gif)
    org = Image.open(gif)
    org = org.convert('RGB')
    for x in range(width):
        for y in range(height):
            pixel = org.getpixel((x, y))
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                trans.putpixel((x, y), pixel)
            #if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                #continue

    org.close()

trans.save('trans.png')
