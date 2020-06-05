import re

def read_sample_file(file):
    with open(file, "r") as f:
        data = f.readlines()
    return data

def find_hosts(data, ignore):
    for line in data:
            if re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line):
                if not ignore in line:
                    print(line.strip())

if __name__ == "__main__":
    ignore = "127.0.0.1"
    file = "/home/coder/python_fortgeschritten/materialien/SampleLog.log"
    raw_data = read_sample_file(file)
    find_hosts(raw_data, ignore)