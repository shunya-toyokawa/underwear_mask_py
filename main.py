import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

img = cv2.imread("input.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#lowerからupperまでの値を1,それ以外を0にする
lower = (130, 100, 0)
upper = (190, 255, 255)
bin_img = cv2.inRange(hsv, lower, upper)

mask_im = Image.fromarray(bin_img)
mask_im.save("mask.png")

# アルファチャンネルを追加する
bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# 2値画像の値が0の画素のアルファ値は0 (透過) にする
bgra[bin_img == 0, 3] = 0


cv2.imwrite("out.png",bgra)
#out = Image.fromarray(bgra)
#out.save("out.png")


