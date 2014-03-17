#!/usr/bin/python

import urllib
import re

def get_next(nothing):

    link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % (nothing)
    f = urllib.urlopen(link).read()
    print f
    get = re.findall('and the next nothing is ([0-9]{3,5})', f)
    if len(get) == 0:
        print "I've failed"
    else:
        get_next(get[0])


if __name__ == "__main__":

#    get_next(12345)
    get_next(8022)
