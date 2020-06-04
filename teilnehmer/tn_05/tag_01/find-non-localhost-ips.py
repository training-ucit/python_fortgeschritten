#!/usr/bin/env python3

import re

logfile = "/home/coder/python_fortgeschritten/materialien/SampleLog.log"

result = []

blacklist = ['127.0.0.1', ]

pattern = r'((\d{1,3}\.){3}\d{1,3})'

re_compiled = re.compile(pattern)

def contains_ip(line):
    m = re_compiled.search(line)
    #m = re.search(pattern, line)
    if m:
        line = line.strip()
        ip = m.group()
        #print(ip)
        if ip not in  blacklist:
            return line
        else:
            return None
    else:
        return None

def get_loglines(logfile):
    with open(logfile) as fh:
        lines = fh.readlines()
    return lines

if __name__ == "__main__":
    lines = get_loglines(logfile)
    for line in lines:
        if contains_ip(line):
            result.append(line)

    print('\n'.join(result))