
import re

class StockValueReader:
    _data = {}
    _header = None

    def __init__(self, fname):
        with open(fname) as fd:
            # Überschriftenzeile gesondert einlesen
            self._header = fd.readline().strip().split(",")
            # Verbleibende Zeilen einlesen und konvertieren
            for line in fd.read().split("\n"):
                if not re.search("^[\t ]*$", line):
                    # Das Datum extrahieren, der Rest in einer Liste
                    # 06/02/2020, $323.34, 21910700, $320.745, $323.44, $318.93
                    date, *values = line.split(",")
                    # Das Datum in seine Bestandteile aufsplitten
                    
                    m, d, y = date.strip().split("/")
                    # dur die Werte durchgehen und gleichzeitig den index erzeugen
                    for i, v in enumerate(values):
                        # Wenn es ein $ ist, das Zeichen entfernen, den Wert umwandeln
                        if v.strip().startswith("$"):
                            values[i] = float(v.replace("$",""))
                        else:
                        # Wenn es eine Ganzzahl ist diese Umwandeln    
                            values[i] = int(v)
                    # aus den Datumsteilen ein deutsches Datum zusammenfügen
                    # und als Key nehmen, dazu die überarbeiteten Werte als Liste zuweisen        
                    self._data[f"{d}.{m}.{y}"] = values

    def __str__(self):
        return str(self._data)

if __name__ == "__main__":
    fname = "/home/coder/python_fortgeschritten/materialien/HistoricalQuotes.csv"
    apple = StockValueReader(fname)
    print(apple)