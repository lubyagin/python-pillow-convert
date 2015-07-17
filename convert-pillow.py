# -* coding: cp1251 -*-
# Python image convert utility
# Python 2.7.10/i386, Pillow 2.9.0

import sys

if len(sys.argv) < 3: sys.exit()
filename_i = sys.argv[1]
filename_o = sys.argv[2]

from PIL import Image # Pillow 2.9.0, replacement for PIL
image = Image.open(filename_i)
print image.format, image.size, image.mode
image.save(filename_o)

sys.exit()
