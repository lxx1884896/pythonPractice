# coding:utf-8
#########################################获取新浪博客评论处的表情包,该处未完成，最终结果在442biaoqingbao.py处
import bs4
from bs4 import BeautifulSoup
import re
import requests
import os
import traceback
import sys
type = sys.getfilesystemencoding()
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()#检查该状态以检查请求是否成功，如果不是200（比如404或其他的），就会抛出异常
        r.encoding = r.apparent_encoding#r.apparent_encoding是从内容中分析出响应的内容编码方式
        return r.text
    except:
        return "产生异常"
html = getHtmlText("http://hits.sinajs.cn/A2/b.html?type=01_13_010_E___0316EN00SIG&pageid=article&msg=&varname=requestId_69333379")
soup = BeautifulSoup(html, "html.parser")
soup=soup.decode('utf-8').encode(type)

print soup