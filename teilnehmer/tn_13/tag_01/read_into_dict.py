#!/usr/bin/python3

file_path = "/home/coder/python_fortgeschritten/materialien/openthesaurus.txt"

def create_dict(path_file):
    list = []
    with open(path_file,"r") as f:
        for line in f:
            if line[0] != "#":
                list.append(line[:-2].split(";"))

    return list

def search_thesaurus(words):
    while True:
        eingabe = input("Ihr Wort: ").strip()
        if eingabe == "--":    
            break
        if isinstance(words, list):
            for zeile in words:
                if eingabe.lower() in map(str.lower, zeile):
                    print(zeile)
        elif isinstance(words, dict):
            if eingabe in words:
                print(words[eingabe])
        else:
            raise Exception("unknown type {}".format(type(words)))


if __name__ == "__main__":
    my_list = create_dict(file_path)  
    search_thesaurus(my_list)
            