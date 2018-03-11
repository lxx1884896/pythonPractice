# coding=utf-8
#########################################锟斤拷取锟截讹拷锟斤拷页锟较憋拷锟斤拷锟�
import bs4
from bs4 import BeautifulSoup
import re
import requests
import os
import traceback

''''' 
锟斤拷锟揭筹拷锟斤拷锟斤拷锟� 
'''


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()#锟斤拷锟斤拷状态锟皆硷拷锟斤拷锟斤拷锟斤拷欠锟缴癸拷锟斤拷锟斤拷锟斤拷锟斤拷锟�200锟斤拷锟斤拷锟斤拷404锟斤拷锟斤拷锟斤拷锟侥ｏ拷锟斤拷锟酵伙拷锟阶筹拷锟届常
        r.encoding = r.apparent_encoding#r.apparent_encoding锟角达拷锟斤拷锟斤拷锟叫凤拷锟斤拷锟斤拷锟斤拷应锟斤拷锟斤拷锟捷憋拷锟诫方式
        return r.text

    except:
        return "锟斤拷锟斤拷锟届常"


'''
锟斤拷锟絚ontent
'''


def getImgContent(url):
    head = {"user-agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=head, timeout=30)
        print("status_code:" + r.status_code)
        r.raise_for_status()
        return r.content
    except:
        return None


''''' 
锟斤拷锟揭筹拷锟斤拷械谋锟斤拷锟斤拷锟斤拷锟斤拷 
'''


def getTypeUrlList(html, typeUrlList):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all("div", attrs={"class": "up"})
    for div in divs:
        a = div.find("div", attrs={"class": "num_1"}).find("a")
        title = a.attrs["title"]
        typeUrl = a.attrs["href"]#typeUrl为锟斤拷锟斤拷锟斤拷锟斤拷锟斤拷锟絬rl
        typeUrlList.append((title, typeUrl))


def getImgUrlList(typeUrlList, imgUrlDict):
    for tuple in typeUrlList:
        title = tuple[0]
        url = tuple[1]
        title_imgUrlList = []
        html = getHtmlText(url)
        soup = BeautifulSoup(html, "html.parser")
        # print(soup.prettify())

        div = soup.find("div", attrs={"class": "img_text"})
        # print(type(div))
        imgDiv = div.next_sibling.next_sibling
        # print(type(imgDiv))
        imgs = imgDiv.find_all("img");
        for img in imgs:
            src = img.attrs["src"]
            title_imgUrlList.append(src)
        imgUrlDict[title] = title_imgUrlList


def getImage(imgUrlDict, file_path):
    head = {"user-agent": "Mozilla/5.0"}
    countdir = 0
    for title, imgUrlList in imgUrlDict.items():
        # print(title+":"+str(imgUrlList))
        try:
            dir = file_path + title
            if not os.path.exists(dir):
                os.mkdir(dir)
            countfile = 0
            for imgUrl in imgUrlList:
                path = dir + "/" + imgUrl.split("/")[-1]#锟斤拷[-1]锟斤拷示锟街革拷锟斤拷锟街拷锟饺★拷锟斤拷锟斤拷锟斤拷锟斤拷冶叩锟� 锟界：abc.gif
                # print(path)
                # print(imgUrl)
                if not os.path.exists(path):
                    r = requests.get(imgUrl, headers=head, timeout=30)
                    r.raise_for_status()
                    with open(path, "wb") as f:
                        f.write(r.content)
                        f.close()
                        countfile = countfile + 1
                        print("锟斤拷前锟斤拷锟斤拷锟侥硷拷锟叫斤拷锟斤拷{:.2f}%".format(countfile * 100 / len(imgUrlList)))
            countdir = countdir + 1
            print("锟侥硷拷锟叫斤拷锟斤拷{:.2f}%".format(countdir * 100 / len(imgUrlDict)))

        except:
            print(traceback.print_exc())
            # print("from getImage 锟斤拷取失锟斤拷")


def main():
    # 锟斤拷锟铰达拷锟教憋拷锟斤拷锟酵诧拷锟斤拷取全锟斤拷锟侥憋拷锟斤拷锟剿ｏ拷只锟斤拷取30页锟斤拷锟斤拷约300锟斤拷锟斤拷锟斤拷锟斤拷锟侥憋拷锟斤拷
    pages = 30
    root = "http://sc.chinaz.com/biaoqing/"  #http://sc.chinaz.com/biaoqing/
    url = "http://sc.chinaz.com/biaoqing/index.html"#http://sc.chinaz.com/biaoqing/index.html
    file_path = "e://biaoqing/"
    imgUrlDict = {}
    typeUrlList = []
    html = getHtmlText(url);
    getTypeUrlList(html, typeUrlList)
    getImgUrlList(typeUrlList, imgUrlDict)
    getImage(imgUrlDict, file_path)
    for page in range(pages):
        url = root + "index_" + str(page) + ".html"
        imgUrlDict = {}
        typeUrlList = []
        html = getHtmlText(url);
        getTypeUrlList(html, typeUrlList)
        getImgUrlList(typeUrlList, imgUrlDict)
        getImage(imgUrlDict, file_path)


main()