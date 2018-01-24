# encoding: UTF-8
import glob as gb
import cv2
import os
from PIL import Image
import PIL.ImageOps
#Returns a list of all folders with participant numbers
for root, dirs, files in os.walk("C://Users//lxx//Desktop//numbers//"):
    for i in range(len(files)):
        imgName=(os.path.join("C://Users//lxx//Desktop//numbers//",files[i]))
        img = cv2.imread(imgName)

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        imgGray=~imgGray
        cv2.imshow("image",imgGray)
        cv2.waitKey(1000)


        # 反转颜色
        # inverted_image = PIL.ImageOps.invert(imgGray)
        # inverted_image.save('new_name.png')
        l = len(files[i])
        cv2.imwrite("C://Users//lxx//Desktop//numbers//"+files[i][0:l - 4]+"Gray.png",imgGray)



