#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
# provide currency name, f.e. Euro, US Dollar ..
# provide period
# call user module readcbr
# plot currency rates with matplotlib

from datetime import datetime
try:
    import matplotlib.pyplot as plt
except:
    print('Matplotlib module was not found. No plot output')
import readcbr

if __name__ == '__main__':
    #cur = 'Euro' startdate = '05.09.2019'  enddate = '30.09.2019'

    dict_currency = readcbr.get_currency_data()
    if dict_currency:
        for v in dict_currency.keys():
            print(v)
        cur = input('Input currency name from list: ')

        if(cur not in dict_currency):
            print('Currency not found. Using euro as a default value')
            cur = 'Euro'

        try: # запрашиваем у пользователя период
            start = input('Input START of period in format YYYY-MM-DD ')
            year, month, day = map(int, start.split('-'))
            start = datetime(year, month, day)
        
            end = input('Input END of period in format YYYY-MM-DD ')
            year, month, day = map(int, end.split('-'))
            end = datetime(year, month, day)
        except ValueError:
            print('Invalid dates. Using period: last month')
            end = datetime.today()
            start = end.replace(day = 1)

        if(start > end):
            print('Invalid dates. Using period: last month')
            end = datetime.today()
            start = end.replace(day = 1)

        # currency code 
        id_code = dict_currency[cur]
        
        # dates to strings dd.mm.YYYY
        datestart = start.strftime('%d.%m.%Y')
        dateend = end.strftime('%d.%m.%Y')
        
        print(10*'---')
        print(id_code, datestart, '-', dateend)
        print(10*'---')

        # call function to get rates
        vals = readcbr.get_rates(id_code, datestart, dateend)
        print(vals)
        if vals:
            plt.plot(*zip(*vals), marker = '.')
            for d, rate in vals:                   
                plt.annotate(round(rate,2), (d, rate), fontsize=6)
            plt.gcf().autofmt_xdate()
            title = f'Currency rates: {cur} on period {datestart} - {dateend}'
            plt.title(title)
            plt.xlabel('Dates')
            plt.ylabel('Russian Ruble')
            plt.grid(visible = True, linestyle = '--', color = 'g')
            plt.show()

    else:
        print('No currency data. Exit script.')