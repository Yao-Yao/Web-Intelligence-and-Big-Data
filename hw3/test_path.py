#!/usr/bin/env python

import os 
def Test2(rootDir): 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        if os.path.isfile(path): 
            infile = open(path)
            print infile.readline()
            infile.close()

Test2('hw3data')
