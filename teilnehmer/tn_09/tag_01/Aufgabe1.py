datei_name = "/home/coder/python_fortgeschritten/materialien/openthesaurus.txt"

with open(datei_name, "r") as fd:
    roh_daten = []
    for zeile in fd.read().split("/n"):
        if zeile[0] != "#":
            roh_daten.append(zeile)

arbeits_daten = []
for zeile in roh_daten:
    arbeits_daten.append(zeile.split(";"))

    print(arbeits_daten)