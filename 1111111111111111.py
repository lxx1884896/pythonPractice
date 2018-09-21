#!/usr/bin/python
# -*- coding:utf-8 -*-
# import os
#
# a=os.path.split('/home/swaroop/byte/code/poem.txt')
# print a
# #print a.split(".")[0]

dict ={'f':2,'b':3,'c':1}


#print max(dict)

dict={dict[key]:key for key in dict}#   dict为{1: 'c', 2: 'f', 3: 'b'}

print max(dict,key=dict.get)#得到最大值所对应的键
print dict