#coding=utf-8


import cv2
img = cv2.imread('contoursImage2.jpg')
b,g,r = cv2.split(img)  #图像拆分与合并
cv2.imshow('b',b)

cv2.imshow('g',g)
cv2.imshow('r',r)
img2=cv2.merge((b,g,r))
cv2.imshow('image2',img2)
cv2.waitKey(0)
import cv2

import numpy as np

BLUE = [255, 0, 0]

img1 = cv2.imread('IMG_20171127_212556.jpg')
# 图片添加边距
replicate = cv2.copyMakeBorder(img1, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 100, 100, 100, 100, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, 100, 100, 100, 100, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 100, 100, 100, 100, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=BLUE)
cv2.imshow('replicate',replicate)
cv2.imshow('reflect',reflect)
cv2.imshow('reflect101',reflect101)
cv2.imshow('wrap',wrap)
cv2.imshow('constant',constant)
cv2.waitKey(0)



















