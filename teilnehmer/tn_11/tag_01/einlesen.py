datei = '../../..materialien/openthesaurus.txt'

with open(datei, 'r') as fd:
    roh_daten = []
    for line in fd.read().split("\n"):
        if not line.startswith("#"):
            roh_daten.append(line)

  arbeits_daten = []
  for line in roh_daten:
      arbeits_daten.append(line.split(";"))


print(arbeits_daten)