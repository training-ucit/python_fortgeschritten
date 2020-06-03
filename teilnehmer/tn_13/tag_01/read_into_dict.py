#!/usr/bin/python3

def create_dict(path_file):
    list = []
    with open(path_file,"r") as f:
        for line in f:
            if line[0] != "#":
                list.append(line[:-2].split(";"))

    return list

def search():
    pass

def main():
    file_path = "/home/coder/python_fortgeschritten/materialien/openthesaurus.txt"
    my_list = create_dict(file_path)
    for x in my_list:
        print(x)

if __name__ == "__main__":
    main()
    
            