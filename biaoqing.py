# -*-coding:utf-8-*-
#########################################��ȡ�ض���ҳ�ϱ����
import bs4
from bs4 import BeautifulSoup
import re
import requests
import os
import traceback

''''' 
���ҳ������ 
'''


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()#����״̬�Լ�������Ƿ�ɹ����������200������404�������ģ����ͻ��׳��쳣
        r.encoding = r.apparent_encoding#r.apparent_encoding�Ǵ������з�������Ӧ�����ݱ��뷽ʽ
        return r.text

    except:
        return "�����쳣"


'''
���content
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
���ҳ���еı�������� 
'''


def getTypeUrlList(html, typeUrlList):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all("div", attrs={"class": "up"})
    for div in divs:
        a = div.find("div", attrs={"class": "num_1"}).find("a")
        title = a.attrs["title"]
        typeUrl = a.attrs["href"]#typeUrlΪ�����������url
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
                path = dir + "/" + imgUrl.split("/")[-1]#��[-1]��ʾ�ָ����֮��ȡ���������ұߵ� �磺abc.gif
                # print(path)
                # print(imgUrl)
                if not os.path.exists(path):
                    r = requests.get(imgUrl, headers=head, timeout=30)
                    r.raise_for_status()
                    with open(path, "wb") as f:
                        f.write(r.content)
                        f.close()
                        countfile = countfile + 1
                        print("��ǰ�����ļ��н���{:.2f}%".format(countfile * 100 / len(imgUrlList)))
            countdir = countdir + 1
            print("�ļ��н���{:.2f}%".format(countdir * 100 / len(imgUrlDict)))

        except:
            print(traceback.print_exc())
            # print("from getImage ��ȡʧ��")


def main():
    # ���´��̱����Ͳ���ȡȫ���ı����ˣ�ֻ��ȡ30ҳ����Լ300���������ı���
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