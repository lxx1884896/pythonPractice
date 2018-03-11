#coding=utf-8
from lxml import etree
from bs4 import BeautifulSoup
import traceback
import  re
import  requests
import sys
import scrapy
import chardet
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')
#获得系统编码格式
type = sys.getfilesystemencoding()
# encode=sys.getdefaultencoding()
# head = {"user-agent": "Mozilla/5.0"}################爬取下面的网页并获取特定内容
# url="https://baike.baidu.com/item/拉布拉多猎犬/452983"
#
# reponse=requests.get(url,allow_redirects=False, headers=head)
#
# soup=BeautifulSoup(reponse.text,'html.parser')
# html = etree.HTML(soup)
# html_data = html.xpath("/html/div[@class='content-warpper']/div[@calss='main-content']/div[@calss='lemma-summary']/div[@calss='para'/a/text()")
#
# print html_data
#
# #print soup.prettify()
#
# #print soup.find_all(('div')
url="https://baike.baidu.com/item/%E6%8B%89%E5%B8%83%E6%8B%89%E5%A4%9A%E7%8C%8E%E7%8A%AC/452983"
head = {"user-agent": "Mozilla/5.0"}
reponse=urllib2.urlopen(url)

reponse=reponse.read()
# soup=BeautifulSoup(reponse,"html.parser")###################35-39行构成一种方法，用soup.find最后 get_text()
# sel=scrapy.selector.Selector(soup)
# #print soup
# a=soup.find("div", attrs={"class": "lemma-summary"}).get_text()
# print a

data= etree.HTML(reponse)
#result = etree.tostring(data, encoding="utf-8")
#print data
result_data=data.xpath("//div[@class='lemma-summary']//text()")
while "\n" in result_data:

     result_data.remove("\n")###############################41-49行构成另一种方法，用etree,用xpath，最后得到的是一个列表
print result_data
print str(result_data).replace("u\'","\'").decode("unicode-escape").encode("utf-8")
# for i in result_data:
#     print i.decode("utf-8")



