#!/usr/bin/env python3

"""
file-transformer reads a structured data file and output another format
e.g. from json to yaml
"""

import json
import yaml
import csv
import os
import sys
import argparse

class FileTransformer:
    def __init__(self, inputfile, outputfile):
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.inputformat = self.guess_format_from_extension(self.inputfile)
        self.outputformat = self.guess_format_from_extension(self.outputfile)
        self.formats = [ 'json', 'csv', 'yml', 'yaml', 'xml' ]
        self.data = {}
        if self.inputformat not in self.formats:
            print("wrong input format: {format}".format(format=self.inputformat))
            sys.exit(1)
        self.load_file(inputfile)

    def guess_format_from_extension(self,filename):
        ext = filename.split('.')[-1]
        return ext

    def load_file(self,inputfile):
        _d = {}
        with open(inputfile) as fh:
            if self.inputformat == "json":
                _d = json.loads(fh.read())
            elif self.inputformat == "yaml" or self.inputformat == "yaml":
                _d = yaml.safe_load(fh)
            elif self.inputformat == "csv":
                for row in csv.DictReader(fh):
                    _d.update(row)
        self.data = _d

    def output_data(self):
        with open(self.outputfile, 'w') as outfh:
            if self.outputformat == "json":
                outfh.write(json.dumps(self.data, indent=2))
            elif self.outputformat == "yaml":
                yaml.dump(self.data, outfh)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--inputfile", help="Input file name")
    parser.add_argument("-o", "--outputfile", help="Output file name")
    args = parser.parse_args()

    ft = FileTransformer(inputfile=args.inputfile, outputfile=args.outputfile)
    ft.output_data()

