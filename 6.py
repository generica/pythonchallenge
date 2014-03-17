#!/usr/bin/python

import zipfile
import re

c = []

def getnext(z, num):
    name = '%s.txt' % (num)
    zz = z.open(name, 'r')
    zzz = z.getinfo(name)
    contents = zz.read()
    f = re.findall('Next nothing is ([0-9]*)', contents)
    c.append(zzz.comment)
    if len(f) == 0:
        print "".join(c)
    else:
        getnext(z, f[0])

z = zipfile.ZipFile('channel.zip', 'r')

getnext(z, '90052')
