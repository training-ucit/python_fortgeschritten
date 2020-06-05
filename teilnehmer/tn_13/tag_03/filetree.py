#!/usr/bin/python3
import os
import sys
import argparse
import fnmatch
import pprint
import glob

def search_file(path, fname):
    result = []
    for root, _, files in os.walk(path):
        if fname in files:
            result.append(os.path.join(root, fname))
    return result

def search_file_pattern(path, fname):
    result = []
    for root, _, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, fname):
                result.append(os.path.join(root, name))
    return result

def b_search_file(startfolder, datei_gesucht):
    return [glob.glob(startfolder + '/**/*' + datei_gesucht, recursive=True)]

parser = argparse.ArgumentParser()
parser.add_argument('--startfolder', '-s', help='Startpunkt der Sucher')
parser.add_argument('--gesuchter_dateiname','-d', help='Name der zu findenden Datei')
args = parser.parse_args()
print(args)
print(args.startfolder)
print(args.gesuchter_dateiname)

pprint.pprint(b_search_file(str(args.startfolder), str(args.gesuchter_dateiname)))
# Aufruf: /usr/bin/python3.6 /home/coder/python_fortgeschritten/teilnehmer/tn_13/tag_03/filetree.py -s "/home/coder/python_fortgeschritten/teilnehmer/tn_13/tag_02" -d ad*
