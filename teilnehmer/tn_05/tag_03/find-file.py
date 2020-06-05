#!/usr/bin/env python3

import argparse
import os
import pprint

parser = argparse.ArgumentParser()
parser.add_argument("--startdir", "-s", default=os.environ['HOME'], help="starting directory")
parser.add_argument("--filename", "-f", help="File name to search for")

args = parser.parse_args()

def search_file(folder, filename):
    result = []
    for root, dirs, files in os.walk(folder):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result

if __name__ == "__main__":
    pprint.pprint(search_file(args.startdir, args.filename))