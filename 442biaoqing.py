import bs4
from bs4 import BeautifulSoup
import re
import requests
import os
import traceback
import sys
import cv2
head = {"user-agent": "Mozilla/5.0"}
url="http://www.sinaimg.cn/uc/myshow/blog/misc/gif/"


for i in range (500):

    file_path = "E://442biaoqing//" + "/E___0" + str(i).zfill(3) + "EN00SIGT.gif"
    if (i==0) :
        continue
    imgUrl=url+"/E___0"+str(i).zfill(3)+"EN00SIGT.gif"
    try:
        r = requests.get(imgUrl, headers=head, timeout=30)
        r.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(r.content)
    except:
        continue


    print i
f.close()
# type = sys.getfilesystemencoding()
# file_path="E://442biaoqing//abc.gif"
#
# url="http://www.sinaimg.cn/uc/myshow/blog/misc/gif/E___0305EN00SIGT.gif"
# head = {"user-agent": "Mozilla/5.0"}
# r = requests.get(url, headers=head, timeout=30)
# r.raise_for_status()
# print r.status_code
#
# with open(file_path, "wb") as f:
#         f.write(r.content)
#
# print type(r.content)