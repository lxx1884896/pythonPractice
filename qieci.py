 #coding= utf-8
import os
import cv2 as cv
file = open('wordBB.txt')
wordBBInMemory = file.readline()
# print(len(wordBBInMemory))  # 226123835
file = open('imnames.txt')
imnamesInMemory = file.readline()
# print(len(imnamesInMemory))  # 18423319

wordBBAtList = wordBBInMemory.split('@')
# print(len(wordBBAtList))  # 858751

imnamesAtList = imnamesInMemory.split('@')
# print(len(imnamesAtList)) # 858751

perImgPathList = [] # 所有的path
perImgList = [] #所有的 result
dirpath = "E:\SynthText\SynthText"
for imnameIndex in range(0,len(imnamesAtList)-1):
    perImgPathList.append(os.path.join(dirpath,imnamesAtList[imnameIndex]))
    # 获得四个点的坐标

for wordBBIndex in range(0,len(wordBBAtList)-1):
    wordBBStarList = wordBBAtList[wordBBIndex].split('*')
    perSplitImgList = {}
    for wordBBStarIndex in range(0,len(wordBBStarList)-1):
        perImgMap = {}
        wordBBUnderlineList  = wordBBStarList[wordBBStarIndex].split('_')
        x_left =  min(wordBBUnderlineList[0],wordBBUnderlineList[3])
        x_right = max(wordBBUnderlineList[1],wordBBUnderlineList[2])
        y_top = max(wordBBUnderlineList[6],wordBBUnderlineList[7])
        y_bottom = min(wordBBUnderlineList[4],wordBBUnderlineList[5])
        perImgMap['leftBottom'] = (x_left,y_bottom)
        perImgMap['rightBottom'] = (x_right,y_bottom)
        perImgMap['rightTop'] = (x_right,y_top)
        perImgMap['leftTop'] = (x_left, y_top)
        perSplitImgList[str(wordBBStarIndex)] = perImgMap # perSplitImgList {"1":{"leftBottom":(1,2),"rightBottom":(2,3),..}},{"2":{...}}
    perImgList.append(perSplitImgList)

# print(perImgList)
# print(perImgPathList)


# opencv operation
#命名方式   本来图片名__0.jpg  比如 0 就是图片的一个切片的序号 双下划线
for  IIndex in range(len(perImgPathList)):
    img = cv.imread(perImgPathList[IIndex])
    for mapkey,mapValue in perImgList[IIndex].items():
        # 注意建好split文件夹
        imgSplitPath ="E:\SynthText\SynthText" +"\split\\" +  os.path.basename(perImgPathList[IIndex]).split('.')[0]  +"__"+mapkey+'.jpg'
        print imgSplitPath

        a =int(mapValue["leftBottom"][0])
        b = int(mapValue["rightBottom"][0])
        c = int(mapValue["leftBottom"][1])
        d = int(mapValue["leftTop"][1])
        # print(type(d))
        # print(d)
        print a,b,c,d
        imgSplit = img[c:d,a:b]
        # imgSplit = img[100:200,100:200]
        cv.imwrite(imgSplitPath,imgSplit)

