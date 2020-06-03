def get_my_list(filepath):
    with open(filepath, 'r') as f:
        rohdaten = [line.strip() for line in f if not '#' in line]
        arbeitsdaten = [i.split(';') for i in rohdaten]
    return arbeitsdaten

def search_list(my_list, search_val):
    for i in my_list:
        if search_val in i:
            return i
            


if __name__ == "__main__":
    arbeitsdaten = get_my_list('/home/coder/python_fortgeschritten/materialien/openthesaurus.txt')
    searcherg = search_list(arbeitsdaten, 'verpassen')
    print(searcherg)