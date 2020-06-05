
class RoloDex:
    def __init__(self, fname):
        self.rolo = []
        self.fname = fname
        self.load(fname)

    def __str__(self):
        return str(self.rolo)

    def load(self, fname):
        self.fname = fname
        with open(fname) as fd:
            roh_daten = fd.readlines() 
        for line in roh_daten:
            worte = line.strip("\n").split(";")
            self.rolo.append({"name":worte[0],
                              "ort": worte[1],
                              "plz": worte[2],
                              "strasse": worte[3]})
        return len(self.rolo)

    def save(self, fname=None):
        if not fname:
            fname = self.fname
        with open(fname, "w") as fd:
            for entry in self.rolo:
                daten = ";".join(entry.values())
                fd.write(daten + "\n")
        
    def search(self, suchwort):
        for entry in self.rolo:
            if suchwort in entry["name"]:
                ergebnis = entry
        return ergebnis

    def new_adr(self, personen_daten):
        self.rolo.append(personen_daten)



if __name__ == "__main__":
    r = RoloDex("/home/coder/python_fortgeschritten/materialien/adressen.csv")
    print(r.search("Willi"))
    r.new_adr({"name": "Elon", "ort":"IRgendwo", "plz":"12345", "strasse":"Woanders"})
    print(r)
    r.save("daddel.txt")