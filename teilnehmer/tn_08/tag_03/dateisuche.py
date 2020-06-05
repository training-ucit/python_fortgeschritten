#!/usr/bin/python3
import argparse
import glob
import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--startfolder', '-s', help='Startpunkt')
parser.add_argument('--datei_gesucht', '-d', help='Zu suchende Datei')
args = parser.parse_args()


def search_file(startfolder, datei_gesucht):
    return [glob.glob(startfolder + '/**/*' + datei_gesucht, recursive=True)]
    
pprint.pprint(search_file(args.startfolder, args.datei_gesucht))