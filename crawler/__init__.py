# -*- coding: utf-8 -*-
import urllib.request
import re
url = "http://news.upc.edu.cn/sdyw/"
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
r = re.compile(r'<a href="/sdyw/(?P<Date>.{10}).*" target="_blank">(?P<Title>.+)</a>')
news = r.findall(html)
for i in range(len(news)):
    date=news[i][0]
    title=news[i][1]
    print(date + " " + title)
    
    #http://www.ituring.com.cn/article/114407