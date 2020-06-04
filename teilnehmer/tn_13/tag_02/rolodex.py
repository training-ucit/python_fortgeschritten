class Person:
    person = {}
    def __init__(self, name, stadt, plz, strasse):
        self.name = name
        self.stadt = stadt
        self.plz = plz
        self.strasse = strasse

    def get(self):
        return str(self.name, self.stadt, self.plz, self.strasse)

    def __str__(self):
        return str(";".join((self.name, self.stadt, self.plz, self.strasse)))


class Rolodex:

    personen = []

    def __init__(self, fname):
        self.fname = fname
        self.load(fname)
    
    def __str__(self):
        return "\n".join([str(entry) for entry in self.personen])
    
    def load(self, path_file):
        with open(path_file, "r") as f:
            roh_daten = f.readlines()
        for line in roh_daten:
            name, stadt, plz, strasse = line.strip("\n").split(";")
            newP = Person(name, stadt, plz, strasse)
            self.personen.append(newP)

    def search(self, suchwort):
        for entry in self.personen:
            if suchwort in entry["name"]:
                print(entry)
                
    def new(self, name, stadt, plz, strasse):
        newP = Person(name, stadt, plz, strasse)
        self.personen.append(newP)

    def save(self, fname = None):
        with open(fname, "w") as f:
            #for entry in self.personen:
            f.write(self.__str__())



if __name__ == "__main__":
    r = Rolodex("/home/coder/python_fortgeschritten/teilnehmer/tn_13/tag_02/adressen.csv")
    print(r)
    print(20*"-")
    r.new("Hans","Puderpest","41469","Dadrüben")
    print(r)
    print(20*"-")
    #r.save("/home/coder/python_fortgeschritten/teilnehmer/tn_13/tag_02/adressen2.csv")

    #r.search("Ulrich")

