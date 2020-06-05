#!/usr/bin/python3
import os
import sys
import argparse

def search_file(folder, fname):
    for root, dirs, files in os.walk(folder):
        if fname in files:
            print(f"found: {os.path.join(root, fname)}")
            


parser = argparse.ArgumentParser()
parser.add_argument('--startfolder', help='Startpunkt der Sucher')
parser.add_argument('--gesuchter_dateiname', help='Name der zu findenden Datei')
args = parser.parse_args()

search_file(args.startfolder, args.gesuchter_dateiname)