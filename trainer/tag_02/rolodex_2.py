class Person:
    def __init__(self, name=None, plz=None, ort=None, strasse=None):
        self.ort = ort
        self.name = name
        self.plz = plz
        self.strasse = strasse

    def daten(self):
        return (self.name, self.plz, self.ort, self.strasse)

        
    def __str__(self):
        return ";".join([self.name, self.plz, self.ort, self.strasse])

class RoloDex:
    def __init__(self, fname):
        self.rolo = []
        self.fname = fname
        self.load(fname)

    def __str__(self):
        return "\n".join([str(entry) for entry in self.rolo])

    def load(self, fname):
        with open(fname) as fd:
            roh_daten = fd.readlines() 
        for line in roh_daten:
            worte = line.strip("\n").split(";")
            self.rolo.append(Person(worte[0], worte[2], worte[1], worte[3]))
        return len(self.rolo)

    def save(self, fname=None):
        if not fname:
            fname = self.fname
        with open(fname, "w") as fd:
            for entry in self.rolo:
                fd.write(str(entry) + "\n")
        
    def search(self, suchwort):
        for entry in self.rolo:
            if suchwort in entry.name:
                ergebnis = entry.daten()
        return ergebnis

    def new_adr(self, personen_daten):
        self.rolo.append(personen_daten)



if __name__ == "__main__":
    r = RoloDex("/home/coder/python_fortgeschritten/materialien/adressen.csv")
    print(r.search("Willi"))
    r.new_adr(Person("Elon", "12345", "IRgendwo", "Woanders"))
    print(r)
    r.save("daddel.txt")
    