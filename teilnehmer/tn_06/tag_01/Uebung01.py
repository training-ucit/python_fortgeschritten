rohdaten = []
with open("/home/coder/python_fortgeschritten/materialien/openthesaurus.txt", "r") as f:
    for line in f:
        if not line.startswith("#"):
            rohdaten.append(line.rstrip("\n"))

thesaurus = []
for zeile in rohdaten:
    thesaurus.append(line.split(";"))

print(rohdaten)