# Liest Daten aus Quelle x, Format an Dateiendung erkennen
# Daten sollen als Dict verarbeitet werden
# Ausgabe als Format der Wahl

import yaml
import json

class FileTransformer:
    daten = {}

    def _find_file_ending(self, fname):
        file = fname.split("/")[-1]
        endung = str(file).split(".")[1]
        print("Dateityp: " + str(endung))
        return endung

    def load(self, fname):
        dateiendung = self._find_file_ending(fname)
        with open(fname, "r") as fd:
            if dateiendung == "yaml":
                self.daten = yaml.load(fd)
            elif dateiendung == "csv":
                pass
            elif dateiendung == "json":
                pass
            elif dateiendung == "xml":
                pass
            else:
                raise Exception("Dateiendung {} nicht gefunden...".format(dateiendung))

    def save(self, fname, zieltyp):
        if zieltyp == "JSON":
            print("Creating JSON")
            with open(fname, 'w') as fd:
                json.dump(self.daten, fd)

    def __str__(self):
        return str(self.daten)

if __name__ == "__main__":
    ft = FileTransformer()
    ft.load("/home/coder/python_fortgeschritten/materialien/config.yaml")
    print(ft)
    ft.save("/home/coder/python_fortgeschritten/teilnehmer/tn_06/tag_02/testergebnis.json", "JSON")