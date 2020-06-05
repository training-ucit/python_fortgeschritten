# fname => Annahme der CSV
# init => Datei laden, intern speichern, zur Nutzung vorbereiten
# Dict{Datum: TT.MM.JJJJ, Liste[Werte]} Liste[Werte] => Kurse ohne $Zeichen als float, Stückzahlen als Int
# __str__ Überladung: Ausgabe als String

class Stock_value_reader:
    import datetime

    fname = "/home/coder/python_fortgeschritten/materialien/HistoricalQuotes.csv"

    def delete_dollar_make_float(self, zahl_as_string):
        # entfernt Dollarzeichen und speicher String als Float
        zahl_as_string.replace("$", "")
        floatalized = float(zahl_as_string)
        return floatalized

    def __init__(self, fname):
        # Variablen
        entries = []
        stock_dict = {}
        # Daten einlesen
        with open(fname, "r") as f:
            data = f.readlines()
        # CSV verarbeiten
        entries = data.strip("\n").split(",")
        # Daten anpassen
        for entry in entries:
            # Datum korrigieren
            datum = entry[0]
            datum = datum.strptime(datum, '%d/%m/%y')
            datum_deutsch = datum.strftime('%d.%m.%y')
            entry[0] = datum_deutsch
            # Close/Last
            close = entry[1]
            f_close = delete_dollar_make_float(close)
            entry[1] = f_close
            # Volume
            volume = entry[2]
            i_volume = int(volume)
            entry[2] = volume
            # Open
            opened = entry[3]
            f_opened = delete_dollar_make_float(opened)
            entry[3] = f_opened
            # High
            high = entry[4]
            f_high = delete_dollar_make_float(high)
            entry[4] = f_high
            # Low
            low = entry[5]
            f_low = delete_dollar_make_float(low)
            entry[5] = f_low

        # zu Dictionary verarbeiten
        for line in data:
            stock_dict[line[0]] = [line[1:]]

        def __str__(self, dict_file):
            for key, value in dict_file:
                print (key + ": " + value)



if __name__ == "__main__":
    
    stock = Stock_value_reader
    stock.__str__()