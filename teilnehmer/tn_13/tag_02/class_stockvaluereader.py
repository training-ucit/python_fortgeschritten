import re


class StockValueReader:
    """ Description	"""
    # dict{key= Datum: TT.MM.Jahr, value= [Werte]}
    daten = {}

    def __init__(self, path=None):
        self.create_dict(path)
#        print(self.daten)
        # zur nutzung vorbereiten

    def __str__(self):
        return self.daten

    def convert_line(self, line):
        """ Convert a line into date and values
        :param line: must looks like [06/02/2020, $323.34, 21910700, $320.745, $323.44, $318.93]
        :returns: date "02.06.2020" , values [float(323.34), int(21910700), float(320.745), float(323.44), float(318.93)]
        """    
        # Aufgabe:
        # Datum Europäisch D/M/Y
        # Kurse ohne $Zeichen als Float
        # Stückzahlen als Int
        pieces = line.split(", ")
        m, d, y = pieces[0].split("/")  # Date
        date = "{}.{}.{}".format(d, m, y)
        f_last = float(pieces[1].replace("$", ""))  # Close/Last
        i_volume = int(pieces[2])  # Volume
        f_open = float(pieces[3].replace("$", ""))  # Open
        f_high = float(pieces[4].replace("$", ""))  # High
        f_low = float(pieces[1].replace("$", ""))  # Low

        values = [f_last, i_volume, f_open, f_high, f_low]

        return date, values

    def create_dict(self, path_file):
        """ Creates a dictionary with the set path_file
        :param path_file: from root path to file string

        :returns: dict(self.daten)
        """ 
        with open(path_file, "r") as f:
            for line in f:
                if "Date" not in line:
                    date, values = self.convert_line(line)
                    self.daten[date] = values
        return self.daten

    def get_date(self, date):
        return self.daten[date]

    def get_date_format(self, date):
        c, v, o, h, l = self.daten[date]
        return "Date\t\tClose/Last\tVolume\t\tOpen\tHigh\t\tLow\n{}\t{}\t\t{}\t{}\t{}\t{}".format(date, c, v, o, h, l)

    def loop_get_date(self):
        """ Loop Input for "get_date" with checking of date and if date is in dictionary.
        :raises: KeyError
        :returns: "Bye!"
        """
        date_regex = re.compile(r"\d{2}.\d{2}.\d{4}")
        while True:
            eingabe = input("Datums Suche: ").strip()
            if eingabe == "--":
                break
            elif date_regex.search(eingabe):
                try:
                    self.get_date(eingabe)
                    print(self.get_date_format(eingabe))
                except KeyError:
                    print("Keine Daten zum Datum enthalten... ")
            else:
                print("Kein gültiges Datum. Bitte im Format DD.MM.YYYY eingeben.")

        return print("Bye!")


if __name__ == "__main__":
    apple = StockValueReader("/home/coder/python_fortgeschritten/materialien/HistoricalQuotes.csv")
    # print(apple.get_date_format("16.04.2020"))
    apple.loop_get_date()
