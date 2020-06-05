"""
Dieses Modul oeffnet und laesst in einem Thesaurus suchen
"""

datei_name = "/home/coder/python_fortgeschritten/materialien/openthesaurus.txt"

def read_file(fname):
    """
    Diese Funktion holt den Inhalt aus einer Datei. 
    - Kommentarzeilen werden ignoriert.
    - "\\n" ist ein neuer Listeneintrag
    :params: fname = string of file path + name + ending
    :return: roh_daten = list of strings
    """
    with open(datei_name, "r") as fd:
        roh_daten = []
        for zeile in fd.read().split("\n"):
            if not zeile.startswith("#"):
                roh_daten.append(zeile)
    return roh_daten

def prepare_data(roh_daten, style="LIST"):
    """
    Die hier mitgegebenen Daten werden in eine Liste oder Dictionary eingetragen.
    ";" ist ein Trennzeichen und wird gesplittet.

    :params: roh_daten = list_of_strings
    :params: style = default(LIST) -> erzeugt Liste , DICT -> erzeugt Dictionary
    :exception: falls eine ungueltiger "style" angegeben wird
    :return: arbeits_daten = list of list of strings OR dict with first key and list if strings
    """
    if style == "LIST":    
        arbeits_daten = []
        for zeile in roh_daten:
            arbeits_daten.append(zeile.split(";"))
    elif style == "DICT":
        arbeits_daten = {}
        for zeile in roh_daten:
            worte = zeile.split(";")
            arbeits_daten[worte[0]] = worte[1:]
    else:
        raise Exception("Invalid argument {}".format(style))
    return arbeits_daten

def search_thesaurus(words):
    """
    Die Suchfunktion des eigentlichen Thesaurus. Bei Eingabe eines Wortes (Ausgabe mit Return) werden alle alternativen mit angezeigt.

    """
    while True:
        eingabe = input("Ihr Wort: ").strip()
        if eingabe == "--":    
            break
        if isinstance(words, list):
            for zeile in words:
                if eingabe in zeile:
                    print(zeile)
        elif isinstance(words, dict):
            if eingabe in words:
                print(words[eingabe])
        else:
            raise Exception("unknown type {}".format(type(words)))


if __name__ == "__main__":
    daten = read_file(datei_name)
    daten = prepare_data(daten, style="LIST")
    search_thesaurus(daten)

