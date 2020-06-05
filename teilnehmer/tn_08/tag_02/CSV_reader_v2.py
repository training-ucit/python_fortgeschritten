class StockValueReader:

    def __init__(self, fname):
        with open(fname) as fd:
            lines = []
            for chars in fd.readlines():
                lines.append(chars.strip().split(","))
            for value in lines[1:]:
                m, d, y = value[0].split("/")
                value[0] = "{}.{}.{}".format(d, m, y)
                value[1] = float(value[1].replace(" $", ""))
                value[2] = int(value[2]. replace(" ", ""))
                value[3] = float(value[3].replace(" $", ""))
                value[4] = float(value[4].replace(" $", ""))
                value[5] = float(value[5].replace(" $", ""))
            print(lines)


apple = StockValueReader("/home/coder/python_fortgeschritten/materialien/HistoricalQuotes.csv")