import feedparser
d=feedparser.parse('http://blog.csdn.net/lanchunhui/rss/list')


print  d['entries']