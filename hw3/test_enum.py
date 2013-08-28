#!/usr/bin/env python

data = ["Humpty Dumpty sat on a wall",
        "Humpty Dumpty had a great fall",
        "All the King's horses and all the King's men",
        "Couldn't put Humpty together again",
        ]
# The data source can be any dictionary-like object
dataenum = enumerate(data)
datasource = dict(enumerate(data))

for (offset,item) in dataenum:
    print offset, item

print datasource
