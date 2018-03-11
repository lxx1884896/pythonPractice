#coding=utf-8
from bs4 import BeautifulSoup
import sys
import requests #################################################python2代码

urls = ['https://www.yrw.com/products/list-direct-all-performance-1-createTimeDesc-{}.html'.format(str(i)) for i in range(1,11)]
# print(urls)

def get_titles(urls,data = None):
    count = 0
    web_data = requests.get(urls)
    soup = BeautifulSoup(web_data.content, 'lxml')
    titles = soup.select(' h3 > a > em > strong')
    for title in titles:

        data = 'title'+':'+title.get_text()
        print data
        count = count+1
    print count

for titles in urls:

    get_titles(titles)
