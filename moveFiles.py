#coding=gbk
import cv2
import os
import numpy as np
import shutil
##########################################将许多文件夹内的文件移到同一个文件夹下
count=0#表情包种类的数目
number=0#表情包计数，最后输出一下总的表情个数
for root, dirs, files in os.walk("E:\\biaoqing\\" ):

    count += 1

    #print  len(files)

    for i in range(len(files)):
        number += 1
        imgdir= (root + "\\" + files[i])


        dirFinal=("E:\\save" + "\\"+str(count) + "_" + files[i])

        print dirFinal
        shutil.copy2(imgdir, dirFinal)

        #Wprint count
print number



