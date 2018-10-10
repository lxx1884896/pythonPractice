#coding=utf-8

#使用python2.7
from os import listdir
from numpy import *

from img2vector import img2vector
from classify0 import classify0
def verifyNumber():
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    hwLabels=[]
    trainMat=zeros((m,1024))
    #print trainingFileList


    for i in range(m):
        trainMat[i,:]=img2vector("trainingDigits/%s" % trainingFileList[i])
        fileName=trainingFileList[i]
        fileStr=fileName.split('.')[0]
        classStr=int(fileStr.split('_')[0])
        hwLabels.append(classStr)
    testFile="test.txt"
    vectorTest=img2vector(testFile)
    res=classify0(vectorTest,trainMat,hwLabels,3)
    print "the number in the file is %d" % res


if __name__=='__main__':
    verifyNumber()







