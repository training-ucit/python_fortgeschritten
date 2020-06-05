# -*- coding: utf-8 -*-
"""
Wie sich die Methoden verhalten, wenn sie nicht in einer Klasse liegen

Anmerkung: global ist nötig, weil globale Variablen in python als übel gelten
"""
_name = None
_ort = None

def __init__(name, ort):
    global _name
    global _ort
    _name = name
    _ort = ort
    

def __str__():
    return "{}, {}".format(_name, _ort)

def save(fname):
    with open(fname, "w") as fd:
        fd.write("{},{}".format(_name, _ort))

def read(fname):
    global _name
    global _ort
    with open(fname, "r") as fd:
        daten = fd.readline()
    daten = daten.strip("\n")
    _name, _ort = daten.split(",")


__init__("Willi", "Hamburg")
print(_name)
print(__str__())
save("daten.txt")
read("/home/coder/daten-2.txt")
print(__str__())