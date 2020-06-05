# Chef benutzt Person zur Datenhaltung
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

class Chef:
    def __init__(self, firma, rolle, abteilung):
        self.firma = firma
        self.rolle = rolle
        self.abteilung = abteilung

    def set_person(self, p):
        self.personen_daten = p

    def __str__(self):
        return str([self.abteilung, self.firma, self.rolle])

c = Chef("uc-it", "trainer", "it")
c.set_person(Person("Willi", "12345", "Dorten", "Irgendwo"))
print(c)
c.personen_daten.name = "Willi"
print(c.personen_daten)