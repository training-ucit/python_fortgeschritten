class Person:
    """
    """
    name = None
    ort = None
    template = "Name: {} - Ort: {}"

    def __init__(self, name=None, ort=None):
        """ Description
        :type self:
        :param self:
    
        :type name:
        :param name:
    
        :type ort:
        :param ort:
    
        :raises:
    
        :rtype:
        :returns:
        """
        self.name = name
        self.ort = ort

    def get_adress_aufkleber(self):
        """ Description
        :type self:
        :param self:
    
        :raises:
    
        :rtype:
        :returns:
        """    
        return self.template.format(self.name, self.ort)


# Testbed
if __name__ == "__main__":
    p = Person()

    p.name = "Willi"

    p2 = Person("Heinz", "Köln")

    print(p.name, p.ort)
    print(p2.name, p2.ort)

    print(p2.get_adress_aufkleber())

    p_daten = []
    werte = dict(Klaus="Hamburg", Heinz="Wedel", Ulrich="Bukarest")
    for k, v in werte.items():
        p_daten.append(Person(k, v))
    print(p_daten[1].get_adress_aufkleber())