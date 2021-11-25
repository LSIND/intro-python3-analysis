#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# provide currency name, f.e. Euro, US Dollar ..
# provide period
# call user module readxml
# plot currency rates with matplotlib

from readxml import *
import matplotlib.pyplot as plt

def main():
    cur = "Euro"
    startdate = "05.09.2019"
    enddate = "30.09.2019"
    tup = getInput(cur, startdate, enddate)
    #print(tup)
    if tup is not None:
        plt.plot(tup[0], tup[1], marker = ".")
        for i, txt in enumerate(tup[1]):
            plt.annotate(round(txt,2), (tup[0][i], tup[1][i]), fontsize=6)
        #plt.gcf().autofmt_xdate()
        title = "Currency rates: {} on period {} - {}".format(cur, startdate,enddate)
        plt.title(title)
        plt.xlabel("Dates")
        plt.ylabel(cur)
        plt.grid(b = True, linestyle = "--")
        plt.show()

main()
