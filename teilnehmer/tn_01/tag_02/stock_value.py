class Stock_value_reader:
 
    def __init__(self, fname):
        
        self.fname = fname

        with open(self.fname, "r") as fd:
            roh_daten = []
            for zeile in fd.read().split("\n"):
                if not zeile.startswith("#"):
                    roh_daten.append(zeile)
        return roh_daten

    def get_adress_aufkleber(self):
        pass

if __name__ == "__main__":

    p = Stock_value_reader.__init__("/home/coder/python_fortgeschritten/materialien/HistoricalQoutes.csv")
