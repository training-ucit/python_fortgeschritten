#!/usr/bin/python3
import re

fname="/home/coder/python_fortgeschritten/materialien/SampleLog.log"

def get_data_file(path_file):
    list = []
    with open(path_file,"r") as f:
        for line in f:
            if line[0] != "#":
                list.append(line[:-2])
    return list


def search_ip(data, ignore):
    string_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    rex = re.compile(string_regex)
    for num, zeile in enumerate(data, start=1):
        m = rex.search(zeile)
        if m != None:
            if ignore != m.group(0):
                print("At Line {num} found \"{zeile}\"".format(num=num, zeile=m.group(0)))


if __name__ == "__main__":
    data = get_data_file(fname)
    search_ip(data, "127.0.0.1")
