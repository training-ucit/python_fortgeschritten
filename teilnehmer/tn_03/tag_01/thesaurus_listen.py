dateiname = '/home/coder/python_fortgeschritten/materialien/openthesaurus.txt'

def read_file(fname):
    with open(dateiname, 'r') as fd:
        roh_daten = []
        
        for zeile in fd.read().split('\n'):
            if not zeile.startswith('#'):
                roh_daten.append(zeile)

def prepare_data(roh_daten, style="LIST"):
    if style == 'LIST':
        arbeits_daten = []
        for zeile in roh_daten:
            arbeits_daten.append(zeile.split(""))
    elif style == 'DICT':
        arbeits_daten = {}
        for zeile in roh_daten:
            worte = zeile.split(";")
            arbeits_daten[worte[0]] - worte[1:]
    else:
        raise Exception("invalid argument {}".format(style))

if __name__ == "__main__":
    daten = read_file(dateiname)
    daten = prepare_data(daten, style='DICT')
