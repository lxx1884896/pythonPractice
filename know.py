#coding=utf-8
import cv2
import os
for a in range(4):
    for root, dirs, files in os.walk("F:/synthtext/ "+" / "+str(a)):
         #print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        imgdir = []

        for i in range(len(files)):
            imgdir.append("F:/synthtext" + "/ " +str(a) + "/ " +files[i])
            print(imgdir[i])
            img = cv2.imread(imgdir[i], cv2.IMREAD_GRAYSCALE)
            if img is None :
                continue
            crop_img = img[0:20,0:200]

            # cropimg.save(os.path.join("F:/new synth text","/", files[i], "_", i,))
            # cv2.SetImageROI(img, (0, 0, img.width / 2, img.height))
            #
            # cv2.SaveImage(os.path.join("F:/new synth text","/", files[i], "_", i, cropimg))
            str_i= str(i)
            l = len(files[i])
            cv2.imwrite("F:/ newsynthtext" + "/ " +str(a) + " / " + files[i][0:l - 4] + "_" + str_i + ".jpg", crop_img)



