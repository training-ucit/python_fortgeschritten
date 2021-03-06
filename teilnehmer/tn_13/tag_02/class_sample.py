class Person:

    def __init__(self, name=None, ort=None):
        self.name = name
        self.ort = ort
        self.template = "Name: {} - Ort: {}"

    def get_addressaufkleber(self):
        return self.template.format(self.name, self.ort)
    
    def __str__(self):
        return self.template.format(self.name, self.ort)
    
    def __repr__(self):
        return "Person('{}', '{}')".format(self.name, self.ort)

if __name__ == "__main__":
    p = Person()
    p.name = "Frank"
    p2 = Person("Lars","Neuss")

    print(p.name, p.ort)
    print(p2)
    print(p.__repr__())

    p3 = eval(p.__repr__())
    print(p3)
#    print(p2.get_addressaufkleber())

    # p_daten = []
    # werte = dict(Klaus="Hamburg", Heinz="Warschau",Rambo="Dschungel")
    # for k,v in werte.items():
    #     p_daten.append(Person(k,v))
    # print(p_daten[2].get_addressaufkleber())