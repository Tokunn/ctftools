#!/usr/bin/evn python2

# set file name
with open("flag.out", "rb") as f:
    binary = f.read()

# set magic number
ind = binary.index('\xff\xd8')
jpeg = binary[ind:]

# set output filename
with open("image.jpg", "wb") as f:
    f.write(jpeg)
