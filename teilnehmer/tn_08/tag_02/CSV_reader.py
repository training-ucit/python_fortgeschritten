class StockValueReader:
    fname = "/home/coder/python_fortgeschritten/materialien/HistoricalQuotes.csv"
    csvdict = {}

    def __init__(self):
        header = []
        liste = self.read_file(self.fname)
        header = liste[0].strip().split(",")
        #print(header[1])
        for ds in liste[1:]:
            wort = ds.split(",")
            m, d, y = wort[0].strip().split("/")
            wort[0] = "{}.{}.{}".format(d, m, y)
            print(wort[0])


    def read_file(self, fname):
        with open(self.fname, "r") as f:
            raw = []
            for zeile in f.read().split("\n"):
                raw.append(zeile)
#            print(raw[0])
        return raw


ergebnis = StockValueReader()