# Chef ist eine Erweiterung von  Person zur Datenhaltung
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

class Chef(Person):
    def __init__(self, firma, rolle, abteilung, name=None, plz=None, ort=None, strasse=None):
        super().__init__(name, plz, ort, strasse)
        self.firma = firma
        self.rolle = rolle
        self.abteilung = abteilung

    def __str__(self):
        ergebnis = super().__str__() + str([self.abteilung, self.firma, self.rolle])
        return ergebnis

c = Chef("uc-it", "trainer", "it", "Willi", "12345", "Dorten", "Irgendwo")
print(c)
c.name = "Willi"
print(c)