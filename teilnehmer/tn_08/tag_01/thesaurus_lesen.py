file = "/home/coder/python_fortgeschritten/teilnehmer/tn_08/tag_01/openthesaurus.txt"
#suche = input("Wonach suchen sie?")
print("Lesen des Thesaurus...")

with open(file, "r") as f:
    raw = []
    for line in f.read().split("\n"):
        if not line.startswith("#"):
            raw.append(line)

# print(raw)
arbeitsliste = []

for line in raw:
    arbeitsliste.append(line.split(";"))

#for x in arbeitsliste:
#    if suche in arbeitsliste:
#        print(x)

