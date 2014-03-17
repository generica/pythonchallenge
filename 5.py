#!/usr/bin/python

import pickle

data = open('banner.p', 'r')
p = pickle.load(data)

for x in p:
    for y in x:
        (char, count) = y
        for i in range(0, count):
            print char,
    print
