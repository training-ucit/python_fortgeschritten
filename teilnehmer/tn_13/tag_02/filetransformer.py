import yaml
import csv
import json
import xml

class FileTransformer:
    daten = {}

    def __str__(self):
        return str(self.daten)

    def load(self, fname):
        #erkennt selbst an Dateiendung die umwandlung
        self.fname_org = fname
        file_end = fname.split(".")[-1]

        with open(self.fname_org, 'r') as stream:
            if file_end == "yaml" or "yml":
                self.daten = yaml.load(stream)
            elif file_end == "json":
                self.daten = json.load(stream)
            elif file_end == "csv":
                self.daten = csv.reader(stream)
            elif file_end == "xml":
                print("ToDo XML")
            else:
                print("Don't know the ending '*."+file_end+"'. Can't read...")
    
    def save(self, fname, file_end):
        with open(fname, "w") as f:
            if file_end == "yaml" or "yml":
                f.write(yaml.dump(self.daten))
            elif file_end == "json":
                f.write(json.dump(self.daten))
            elif file_end == "csv":
                f.write(csv.writer(self.daten))
            elif file_end == "xml":
                print("ToDo XML")
            else:
                print("Don't know the ending '*."+file_end+"'. Can't write...")

        


if __name__ == "__main__":
    ft = FileTransformer()
    #---- 4yml ----
    #ft.load("/home/coder/python_fortgeschritten/materialien/config.yaml")
    #print(ft)
    #ft.save("/home/coder/python_fortgeschritten/teilnehmer/tn_13/tag_02/testergebnis.yml","yml")

    ft.load("/home/coder/python_fortgeschritten/materialien/adressen.csv")

    #ft.load("/home/coder/python_fortgeschritten/materialien/config.json")
    print(ft)
    ft.save("/home/coder/python_fortgeschritten/teilnehmer/tn_13/tag_02/testergebnis.json","json")