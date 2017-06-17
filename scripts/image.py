import sys, cv2
import numpy as np

source_path = sys.argv[1]
dest_path = sys.argv[2]

im = cv2.imread(source_path)
im = cv2.resize(im, (64, 64))
blue, green, red = cv2.split(im)

red /= 3
mask = (red > 250).astype(int) + (blue < 25).astype(int) + (green < 25).astype(int)
red[mask != 0] = 255

cv2.imwrite(dest_path, red)