#coding=utf-8
from bs4 import  BeautifulSoup
import urllib2
import re
import requests###############################用scrapy和xpath爬取东西并存入文件
import sys
import scrapy
import urllib
head = {"user-agent": "Mozilla/5.0"}
# 设置编码
reload(sys)
sys.setdefaultencoding('utf-8')
# 获得系统编码格式
type = sys.getfilesystemencoding()
url="https://baike.baidu.com/item/%E6%8B%89%E5%B8%83%E6%8B%89%E5%A4%9A%E7%8C%8E%E7%8A%AC/452983"

reponse=requests.get(url,headers=head)


sel=scrapy.selector.Selector(reponse)

results=sel.xpath("//div[@class='lemma-summary']//text()").extract()
while "\n" in results:

     results.remove("\n")
#print type(result)
# for result in results:
#     ok=result.xpath("a/text()").extract()
#     print result
print results
a=(str(results).replace("u\'","\'")).decode("string_escape")#.decode("unicode-escape").encode("utf-8")
print a
#print str(result).replace("u\'","\'").decode("unicode-escape").encode("utf-8")
with open("321.txt" ,"wb")   as f:
    f.write(a)
    f.close()