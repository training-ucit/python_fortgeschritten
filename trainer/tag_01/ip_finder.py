import re

fname="/home/coder/python_fortgeschritten/materialien/SampleLog.log"

with open(fname) as fd:
    roh_daten = fd.readlines()

rex = re.compile(r"(((\d{1,3}\.){3})(\d{1,3}))")
for zeile in roh_daten:
    m = rex.search(zeile)
    if m:
        if not "127.0.0.1" in zeile:
            print(zeile.strip())
            print(m.groups())
            print("Maschinen-IP {}".format(m.group(4)))

