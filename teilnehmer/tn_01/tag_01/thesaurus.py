#!/usr/bin/python3

def read_data(fnmae):
  with open('fname', r) as f:
    lines = f.read().splitlines()
    return lines
  f.close()



def prepare_data(lines):
  thesaurus=[]

  for line in lines:
    if not line.startswith("#"):
      thesaurus.append(line.split(";"))



if __name__ == "__main__":

   daten = read_data(openthesaurus.txt)