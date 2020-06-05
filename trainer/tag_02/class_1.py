class Person:
    _name = None
    _ort = None

    def __init__(self, name, ort):
        self._name = name
        self._ort = ort

    def __str__(self):
        return "{}, {}".format(self._name, self._ort)

    def save(self, fname):
        with open(fname, "w") as fd:
            fd.write("{},{}".format(self._name, self._ort))

    def read(self, fname):
        with open(fname, "r") as fd:
            daten = fd.readline()
        daten = daten.strip("\n")
        self._name, self._ort = daten.split(",")


p = Person("Willi", "Hamburg")
print(p)
p.save("daten.txt")
p.read("/home/coder/daten-2.txt")
print(p)