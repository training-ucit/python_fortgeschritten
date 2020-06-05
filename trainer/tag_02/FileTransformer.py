import json
import yaml
import csv
import xml
import sys

class FileTransformer:
    daten = dict()
    ftypes = ["json", "yaml", "csv", "xml"]

    def _yaml_loader(self, fd):
        self.daten = yaml.load(fd)

    def _json_loader(self, fd):
        self.daten = json.load(fd)
        
    def _csv_loader(self, fd):
        pass

    def _xml_loader(self, fd):
        pass

    def _yaml_writer(self, fd):
        yaml.dump(self.daten, fd)

    def _json_writer(self, fd):
        json.dump(self.daten, fd)
        
    def _csv_writer(self, fd):
        pass
    def _xml_writer(self, fd):
        pass

    def _check_ftype(self, ftype):
        if ftype not in self.ftypes:
            raise Exception(f"unknown fileftype {ftype}")

    def load(self, fname):
        ftype = fname.split(".")[-1]
        self._check_ftype(ftype)
        with open(fname) as fd:
            if ftype == "yaml":
                self._yaml_loader(fd)
            elif ftype == "json":
                self._json_loader(fd)
            elif ftype == "csv":
                self._csv_loader(fd)
            else:  # ftype == "xml"
                self._xml_loader(fd)

    def save(self, fname, ftype):
        self._check_ftype(ftype)
        with open(fname, "w") as fd:
            if ftype == "yaml":
                self._yaml_writer(fd)
            elif ftype == "json":
                self._json_writer(fd)
            elif ftype == "csv":
                self._csv_writer(fd)
            else: # ftype == "xml"
                self._xml_writer(fd)
            
    def __str__(self):
        return str(self.daten)


if __name__ == "__main__":
    ft = FileTransformer()
    ft.load("/home/coder/python_fortgeschritten/materialien/config.yaml")
    print(ft)
    ft.save("testergebnis.json", "json")