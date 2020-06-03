#!/usr/bin/env python3
import os
filename = '/home/coder/python_fortgeschritten/materialien/openthesaurus.txt/openthesaurus.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line)