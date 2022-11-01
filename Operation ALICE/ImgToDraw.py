

import numpy as np
import sys
import cv2
#Test kode

im = cv2.imread("test.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow('Color image', im)

print(len(im[0]))

new_arr = []
for i in range(len(im)):
    for j in range(len(im[i])):
        if im[i][j] < 200:
            new_arr.append([i,j])
        else:
            continue

print(new_arr)