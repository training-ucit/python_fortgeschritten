#!/usr/bin/python3
import os
import sys
import argparse



def search_file(filename, search_path):
   """Given a search path, find file
   """
   file_found = 0
   paths = string.split(search_path, pathsep)
   for path in paths:
      if exists(join(path, filename)):
          file_found = 1
          break
   if file_found:
      return abspath(join(path, filename))
   else:
      return None



class Open_file:
    pass

class Arg:
    parser = argparse.ArgumentParser()
    parser.add_argument('--startfolder', help='Startpunkt der Sucher')
    parser.add_argument('--gesuchter_dateiname', help='Name der zu findenden Datei')
args = parser.parse_args()
print(args)
print(args.startfolder)
print(args.gesuchter_dateiname)