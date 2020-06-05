import yaml
import json

class FileTransformer:
    daten = dict()

    def load(self, fname):
        if "yaml" or "YAML" or "yml" or "YML" in fname:
            with open(fname, "r") as fd:
                self.daten = yaml.safe_load(fd)
        else:
            print("ist kein YAML!")


    def save(self, fname, typ):
        if typ == "JSON" or "json" or "js" or "JS":
            with open(fname, "w") as fd:
                fd.write(json.dumps(self.daten))

    def __str__(self):
        return str(self.daten)

if __name__ == "__main__":
    ft = FileTransformer()
    ft.load("/home/coder/python_fortgeschritten/materialien/config.yaml")
    print(ft)
    ft.save("testergebnis.json", "JSON")