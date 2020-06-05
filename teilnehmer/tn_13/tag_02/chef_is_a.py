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


class Chef(Person):
    def __init__(self, firma, rolle, abteilung, name=None, stadt=None, plz=None, strasse=None):
        Person.__init__(self, name, stadt, plz, strasse)
        self.firma = firma
        self.rolle = rolle
        self.abteilung = abteilung

    def __str__(self):
        return Person.__str__(self) + str([self.firma, self.rolle, self.abteilung])


c = Chef("Vodafone", "Operator", "Technik", "Rafael","Mainz","12345","Weghier")
print(c)
c.name = "Mike"
print(c)