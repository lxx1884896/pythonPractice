#coding=gbk
import cv2
import os
import numpy as np
import shutil
##########################################������ļ����ڵ��ļ��Ƶ�ͬһ���ļ�����
count=0#������������Ŀ
number=0#�����������������һ���ܵı������
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



