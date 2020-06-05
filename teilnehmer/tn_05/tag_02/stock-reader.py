#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Stock_value_reader:
    """
    hübsche Klasse
    """
    def __init__(self, filename):
        self.filename = filename
        self.values = {}
        self.parse_infile(self.filename)

    def parse_infile(self, infile):
        with open(infile) as fh:
            for line in fh.readlines():
                if line.startswith("Date"):
                    continue
                line = line.strip()
                split_line = line.split(', ')
                date = split_line[0]
                date = self.mangle_date(date)
                stock_values = split_line[1:]
                self.values.update({date: [self.strip_dollarsign(v) for v in stock_values]})
    
    def strip_dollarsign(self, invalue):
        return invalue.replace("$", "")
    
    def mangle_date(self, date):
        #print(date)
        month,day,year = date.split('/')
        return '{day}.{month}.{year}'.format(day=day, month=month, year=year)

    def __repr__(self):
        outstring = "Date, Close/Last, Volume, Open, High, Low"
        for k, v in self.values.items():
            outstring += "{date}, {Close}, {Volume}, {Open}, {High}. {Low}\n".format(date=k, Close=float(v[0]), Volume=v[1], Open=float(v[2]), High=v[3], Low=v[4])
        return outstring

if __name__ == "__main__":
    svr = Stock_value_reader("/home/coder/python_fortgeschritten/materialien/HistoricalQuotes.csv")
    print(svr)