#!/usr/bin/python3
import os
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--startfolder', help='Startpunkt der Sucher')
parser.add_argument('--gesuchter_dateiname', help='Name der zu findenden Datei')
args = parser.parse_args()
print(args)
print(args.startfolder)
print(args.gesuchter_dateiname)