import yaml, json, sys

class FileTransformer:
    daten = dict()

    def load(self, fname):
        #with open (self.fname, "r") as fd:
        self.daten = yaml.load(open(self.fname))
        print(self.daten)

    def save(self, fname, typ):
        pass


    def __str__(self):
        return str(self.daten)

sys.stdout.write(json.dumps(yaml.load(sys.stdin), sort_keys=True, indent=2))


if __name__ == "__main__":
    ft = FileTransformer()
    ft.load("/home/coder/python_fortgeschritten/materialien/config.yaml")
    print(ft)
    #ft.save("testergebnis.json", "JSON")