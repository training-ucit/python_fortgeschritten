"""
Module that reads 
"""
datei_name = "/home/coder/python_fortgeschritten/materialien/openthesaurus.txt"

def read_file(fname):
    """
    read_file reads text data in openthesaurus format into list.

    - Comment lines are ignored
    - \n are stripped

    :fname: String, path of data file
    :return: list of strings
    """
    with open(datei_name, "r") as fd:
        roh_daten = []
        for zeile in fd.read().split("\n"):
            if not zeile.startswith("#"):
                roh_daten.append(zeile)
    return roh_daten

def prepare_data(roh_daten, style="LIST"):
    """
    prepare_data makes a searchable dict or list out of a list of strings

    - sep. char is ";" for the string with the words
    - trhows Exception if styl is unknown

    :roh_daten: list of strings
    :style: type of datastructure to generate (DICT, LIST)

    :returns: list of list if style: LIST
              dict of list if style: DICT
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

