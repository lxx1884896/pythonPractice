#coding=utf-8
import bs4
import telnetlib
from bs4 import BeautifulSoup
from requests import RequestException
import requests
#############################################从西刺网站获取代理并判断可用性
url = 'http://www.xicidaili.com/wt'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}
ip_list = []
def get_ip_list(url, headers):
    """ 从代理网站上获取代理"""

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    ul_list = soup.find_all('tr', limit=20)

    #print(len(ul_list))
    for i in range(1, len(ul_list)):#从第2个tr到第20个tr（第一个tr里是其他的，不是IP，因此舍弃）
        line = ul_list[i].find_all('td')
        ip = line[1].text
        port = line[2].text
        address = ip + ':' + port
        ip_list.append(address)

    return ip_list
def get_proxy(aip):
    """构建格式化的单个proxies"""
    proxy_ip = 'http://' + aip
    proxy_ips = 'https://' + aip
    proxies = {'https': proxy_ips, 'http': proxy_ip}
    return proxies
def print_ip(proxies):
    """利用http://www.whatismyip.com.tw/显示访问的ip"""
    cookies = {
        'sc_is_visitor_unique': 'rx6392240.1508897278.298AFF0AE2624F7BC72BADF517B67AEE.2.2.2.2.2.2.1.1.1',
    }

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
    }
    url = 'http://www.whatismyip.com.tw/'
    # try:
    #     page = requests.get(url, headers=headers, proxies=proxies)
    # except:
    #     print(str(proxies) + 'is wrong')
    # else:
    #     soup = BeautifulSoup(page.text, 'lxml')
    #     my_ip = soup.find('b')
    #     if my_ip==None: #########################判断是否非空的原因是：当为空时，就无法使用.text获取到标签内容了并且会
    #         return False#########################报错，说没有text这个属性，值得引起注意
    #
    #     print('成功连接' + str(my_ip.text))
   # page = requests.get(url, headers=headers, cookies=cookies, proxies=proxies)

    hd, port1 = proxies.split(':')
    #print hd,port1
    try:
        telnetlib.Telnet(hd, port=str(port1), timeout=20)
    except :
        print(str(hd) + 'is wrong')
    else:



        print('成功连接'+ str(hd))


if __name__ == '__main__':
    ip_list=get_ip_list(url,headers)
    print (ip_list)
    for i in range (len(ip_list)):
        #proxies=get_proxy(ip_list[i])
        print_ip(ip_list[i])






