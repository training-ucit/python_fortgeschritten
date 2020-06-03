#!/usr/bin/env python3
import sys

searchterm = sys.argv[1]

searchdict = {}

thesaurus = "/home/coder/python_fortgeschritten/materialien/openthesaurus.txt"

def read_thesaurus(filename):
    outlines = []
    with open(thesaurus) as f:
        for l in f.readlines():
            if not l.startswith('#'):
                l = l.strip()
                outlines.append(l)
    return outlines

def line2dict(line):
    d = {}
    lineitems = line.split(';')
    key = lineitems[0]
    values = lineitems[1:]
    d[key] = values
    return d

if __name__ == "__main__":
    lines = read_thesaurus(thesaurus)
    for line in lines:
        searchdict.update(line2dict(line))
    if searchterm in searchdict:
        print(" ".join(searchdict[searchterm]))