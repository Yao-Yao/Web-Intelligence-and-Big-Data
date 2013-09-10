#!/usr/bin/env python
# -*- coding: cp936 -*-
import mincemeat
import os
from stopwords import *

# data = ["Humpty Dumpty sat on a wall",
#         "Humpty Dumpty had a great fall",
#         "All the King's horses and all the King's men",
#         "Couldn't put Humpty together again",
#         ]
# # The data source can be any dictionary-like object
# datasource = dict(enumerate(data))

datasource = {}
dataDir = 'hw3data'
for lists in os.listdir(dataDir): 
    path = os.path.join(dataDir, lists) 
    if os.path.isfile(path): 
        infile = open(path)
        # paper-id:::author1::author2::...::authorN:::title
        for line in infile:
            l = line.split(':::')
            authors = l[1].split('::')
            title = l[2].rstrip()
            title = title.replace(',','')
            title = title.replace('.','')
            words = [w for w in title.split() if not w in allStopWords.keys()]
            for author in authors:
                if author in datasource:
                    datasource[author] += words # += is equivalent to append()
                else:
                    datasource[author] = words
        infile.close()


# print datasource

def mapfn(k, v):
    for w in v:
        yield k, w

def reducefn(k, vs):
    stat = {}
    for w in vs:
    	if w in stat:
    		stat[w] += 1
    	else:
    		stat[w] = 1
    return stat

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
# print results

outfile = open('out.txt', 'w')
for k in results.keys():
	outfile.write(str(k)+'\n')
    # sorted(results[k].items(), key=lambda x:x[1], reverse=True)
	outfile.write(str(sorted(results[k].items(), key=lambda x:x[1], reverse=True))+'\n\n\n')
outfile.close()

