#coding=utf-8
import cv2
import os



imgdir=[]

for q in range (4):
    q_str=str(q)
for root, dirs, files in os.walk(" F:/synthtext" +"/" + "q_str "):    #
    # print(root) #当前所有目录（包括子目录）路径
    #     #print(dirs) #当前路径下(包括子目录路径下)所有子目录
    # print(files) #当前路径下所有非目录子文件

        for i in range(len(files)):

            imgdir.append ("F:/synth text"+ "/"+files[i])
            img=cv2.imread(imgdir[i], cv2.IMREAD_GRAYSCALE)
            crop_img= img[0:20, 0:30]

            # cropimg.save(os.path.join("F:/new synth text","/", files[i], "_", i,))
            # cv2.SetImageROI(img, (0, 0, img.width / 2, img.height))
            #
            # cv2.SaveImage(os.path.join("F:/new synth text","/", files[i], "_", i, cropimg))
            i_str=str(i)
            l=len(files[i])
            cv2.imwrite("F:/newsynthtext"+"/"+q_str+"/"+files[i][0:l-4]+"_"+i_str+".jpg",crop_img)



