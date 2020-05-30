import os
import sys
from PIL import Image

# import scikit-image
import numpy as np

# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO

directory = './input'

stepcount = 0

xvar = 400

yt_red = (255, 0, 0, 255)
twitch_purple = (62, 33, 109)

# tgt_px = yt_logo
tgt_cl = twitch_purple



counter = 0

for file in os.listdir(directory):
    current = os.path.join(directory, file)
    print(current)
    img = Image.open(current).convert('RGBA')
    px = img.load()
    clr = px[2000, 310]

    try:
        if clr == tgt_cl:
            print(clr, "px match")
            newfile = os.path.join(directory, "Twitch_" + file[12:])
            os.rename(current, newfile)
            counter += 1

        else:
            print(clr)

    except:
        print("Out of Range")

print(counter, "found")

# iml = img.load()
# iar = np.array(img.getdata())
# getpixel(iml, 100,100)

# iar = np.asarray(img)
# test = iar.view(dtype=np.int8).reshape(4, -4).tolist()


# print(iar, "np array")
# print(test)