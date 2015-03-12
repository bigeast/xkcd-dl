#!/bin/env python2
import urllib2
import re
from HTMLParser import HTMLParser
import sys
def xkcd_dl(low, high):
    for n in range(low, high + 1):
        a = urllib2.urlopen('https://xkcd.com/' + str(n))
        f = a.read()
        imgurl, title, alt = re.findall(r'<img src="([^"]*)" title="([^"]*)" alt="([^"]*)"',f)[0]
        title = HTMLParser().unescape(title)
        print(str(n).ljust(3), imgurl.ljust(60), alt)
        # xkcd = open('xkcd' + str(n) + '.html', 'wb')
        # xkcd.write(f)
        # xkcd.close()
        imgfile = open('xkcd ' + str(n) + ':' + alt + '.jpg', 'wb')
        img = urllib2.urlopen(imgurl).read()
        imgfile.write(img)
        imgfile.close()

Usage = "xkcd.py fromID [toID]"
argc = len(sys.argv)
if argc > 3:
    print(Usage)
else:
    if argc == 3:
        low = int(sys.argv[1])
        high = int(sys.argv[2])
    elif argc == 2:
        low = int(sys.argv[1])
        high = low + 10
    else:
        low = 0
        high = low + 10
    xkcd_dl(low, high)
