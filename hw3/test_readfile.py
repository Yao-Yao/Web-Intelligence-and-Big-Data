#!/usr/bin/env python

infile = open('c0001', 'r')

datasource = {}

line = infile.readline()
while line:
    l = line.split(':::')
    for author in l[1].split('::'):
        print l[1]
        if datasource.has_key(author):
            datasource[author] += ' ' + l[2]
        else:
            datasource[author] = l[2]
    line = infile.readline()

print datasource

infile.close()
