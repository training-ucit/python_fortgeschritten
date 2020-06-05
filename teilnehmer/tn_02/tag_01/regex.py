import re

def match_ip(s):
    # re compile bereitet Ausdruck vorbei
    re_ipaddress = re.compile(r'[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]')
    
    if re_ipaddress.search(s) and not '127.0.0.1' in s):
        return True
    else:
        return False

def main():
    filepath = '/home/coder/python_fortgeschritten/materialien/SampleLog.log'
    matching_list = []
    with open(filepath, 'r') as f:
        # matching_list = [i for i in f if match_ip(i)]
        # print(matching_list)
        for line in f:
            if match_ip(line):
                print(line.strip())


if __name__ == '__main__':
    main()