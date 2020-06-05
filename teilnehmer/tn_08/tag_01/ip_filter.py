import re
# Load file into (line-)object

def read_file():
    fname = open("/home/coder/python_fortgeschritten/materialien/SampleLog.log", "r")
    lines = fname.readlines()
    return lines


def search_ip(lines):
    filtered_list = []
    filtered_list.append(re.findall("\d{1,3}\.\d{1,3}\."))
    return filtered_list


if __name__ == "__main__":
    list = read_file()
    print(search_ip(list))
