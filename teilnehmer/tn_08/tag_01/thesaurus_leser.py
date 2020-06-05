"""
Module that reads Openthesaurus source and gives synonyms/alternatives to the searched word
- Author: XYZ
"""

datei_name = "/home/coder/python_fortgeschritten/materialien/openthesaurus.txt"

def read_file(fname):
    """
    read_file reads text data in openthesaurus format into list

    - Comment lines are ignored
    - \n are stripped

    :fname: String, path of data file
    :returns: list of strings
    """
    with open(datei_name, "r") as fd:
        roh_daten = []
        for zeile in fd.read().split("\n"):
            if not zeile.startswith("#"):
                roh_daten.append(zeile)
    return roh_daten

def prepare_data(roh_daten, style="LIST"):
    """
    prepare_data creates either a list or a dictionary, depending on user-input

    - sep. char is ";" for the string containing words
    - throws exception 
    - Comment lines are ignored

    :fname: String, path of data file
    :return: list of strings
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

