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


class Chef:
    def __init__(self, firma, rolle, abteilung):
        self.firma = firma
        self.rolle = rolle
        self.abteilung = abteilung

    def set_person(self, p):
        self.personen_daten = p

    def __str__(self):
        return str([self.firma, self.rolle, self.abteilung])


c = Chef("Vodafone", "Operator", "Technik")
c.set_person(Person("Rafael","Mainz","12345","Weghier"))
print(c)
c.personen_daten.name = "Mike"
print(c.personen_daten)