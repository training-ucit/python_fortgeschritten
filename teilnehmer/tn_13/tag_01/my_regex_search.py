#!/usr/bin/python3
import re

fname="/home/coder/python_fortgeschritten/materialien/SampleLog.log"

def get_data_file(path_file):
    """
    Diese Funktion holt den Inhalt aus einer Datei.
    :params: path = string - file path + name + ending
    :return: list
    """
    list = []
    with open(path_file,"r") as f:
        for line in f:
            if line[0] != "#":
                list.append(line[:-2])
    return list


def search_ip(data, ignore):
    """
    Diese Suche erkennt in Zeilen IP Adressen + Ignoriert angegebene IP Adressen.
    Data sollte eine Liste sein und Ignore wird in eine Regex umgewandelt.
    :params: data = list
    :params: ignore = string
    :return: None   
    """
    string_regex = r"\d{1,3}(\.[\d]{1,3}){3}"
    ignore_regex = ignore
    rex = re.compile(string_regex)
    ign = re.compile(ignore_regex)
    for num, zeile in enumerate(data, start=1):
        m = rex.search(zeile)
        if m != None:
            if not ign.search(m.group(0)):
                print("At Line {num} found \"{zeile}\"".format(num=num, zeile=m.group(0)))


if __name__ == "__main__":
    data = get_data_file(fname)
    search_ip(data, "127")
