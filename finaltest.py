#coding=utf-8
import requests
import bs4
from bs4 import BeautifulSoup
import sys
#Cookie = "PHPStat_First_Time_10000011=1480428327337; PHPStat_Cookie_Global_User_Id=_ck16112922052713449617789740328; PHPStat_Return_Time_10000011=1480428327337; PHPStat_Main_Website_10000011=_ck16112922052713449617789740328%7C10000011%7C%7C%7C; VISITED_COMPANY_CODE=%5B%22600064%22%5D; VISITED_STOCK_CODE=%5B%22600064%22%5D; seecookie=%5B600064%5D%3A%u5357%u4EAC%u9AD8%u79D1; _trs_uv=ke6m_532_iw3ksw7h; VISITED_MENU=%5B%228451%22%2C%229055%22%2C%229062%22%2C%229729%22%2C%228528%22%5D"
type = sys.getfilesystemencoding()
def getHtmlText(url):
    try:
        r = requests.get(url,headers, timeout=30)
        r.raise_for_status()#检查该状态以检查请求是否成功，如果不是200（比如404或其他的），就会抛出异常
        r.encoding = r.apparent_encoding#r.apparent_encoding是从内容中分析出响应的内容编码方式
        return r.content
    except:
        return "产生异常"
#url = "http://hits.sinajs.cn/A2/b.html?type=01_07_000_000&pageid=article&msg=&varname=requestId_16009551"

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Host' : 'hits.sinajs.cn',
    'Referer': 'http://blog.sina.com.cn/s/blog_169af45200102x57h.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
   # 'Cookie': Cookie,

}

# req = requests.get(url, headers)
# html = req.text
# print html
# soup = BeautifulSoup(html, "html.parser")
# print soup
html = getHtmlText("http://www.sinaimg.cn/uc/myshow/blog/misc/gif/E___0315EN00SIGT.gif")
print html
soup = BeautifulSoup(html, "html.parser")
soup=soup.decode('utf-8').encode(type)
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print soup