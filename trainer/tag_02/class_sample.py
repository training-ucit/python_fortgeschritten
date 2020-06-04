class Person:
    """
    """
    name = None
    ort = None
    template = "Name: {} - Ort: {}"

    def __init__(self, name=None, ort=None):
        self.name = name
        self.ort = ort

    def get_adress_aufkleber(self):
        return self.template.format(self.name, self.ort)

    def __str__(self):
        return self.template.format(self.name, self.ort)

    def __repr__(self):
        return "Person('{}', '{}')".format(self.name, self.ort)

    def __geheim(self):
        pass

    def _privat(self):
        pass

# Testbed
if __name__ == "__main__":
    p = Person()

    p.name = "Willi"

    p2 = Person("Heinz", "Köln")

    print(p)
    print(p.__repr__())

    p3 = eval(p.__repr__())
    print(p3)

    p3._privat()
    #p3.__geheim()
    #print(p.name, p.ort)
    #print(p2.name, p2.ort)

    #print(p2.get_adress_aufkleber())

    #p_daten = []
    #werte = dict(Klaus="Hamburg", Heinz="Wedel", Ulrich="Bukarest")
    #for k, v in werte.items():
    #    p_daten.append(Person(k, v))
    #print(p_daten[1].get_adress_aufkleber())
