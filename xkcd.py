#!/bin/env python2
import urllib2
import lxml.html
import sys
import time
def xkcd_dl(low, high):
    all_size = 0
    all_s = time.time()
    for n in range(low, high):
        if n == 404:
            continue
        s = time.time()
        url = 'https://xkcd.com/' + str(n)
        content = urllib2.urlopen(url)
        doc_tree = lxml.html.fromstring(content.read())
        img = doc_tree.xpath('//img')[1]
        comic_url = img.attrib['src']
        comic_title = img.attrib['alt']
        comic_declare = img.attrib['title']
        comic_file = open('xkcd ' + str(n) + ':' + comic_url.split('/')[-1], 'wb')
        comic = urllib2.urlopen(comic_url).read()
        comic_file.write(comic)
        comic_file.close()
        t = time.time()
        file_size = len(comic)
        all_size += file_size;
        print(str(n).ljust(4), comic_url.ljust(60), "%.1f" % (file_size / 1024.0) + "K",  comic_title, "%.4f" % (t - s))
    all_t = time.time()
    print("%d comics downloaded in %d s, average download time is %.4f s." % (high - low, all_t - all_s, ((all_t - all_s) / (high - low))))
    all_size_str = "%.1f" % (all_size / 1024.0)  + "K" if all_size < 1024 * 1024 else "%.1f" % (all_size / 1024.0 / 1024.0)  + "M"
    print("Total size: " + all_size_str);

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
        low = 1
        high = low + 10
    xkcd_dl(low, high)
# xkcd.com/404 doesn't exist.
# xkcd.com/934 name is 'MAC/PC'.
# compiled regex seems didn't improve the performance, comic 755~934 take 179s to download.
