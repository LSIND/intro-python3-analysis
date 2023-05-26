#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
'''reads currency rates from Central Bank of Russia (cbr.ru) in XML-format using module xml.etree.ElementTree'''

from urllib.request import urlopen
from xml.etree.ElementTree import parse

def get_xmldoc(url):
    try:
        resp = urlopen(url) # xml
        if(resp.status == 200):
            xml = parse(resp)
    except Exception as e:
        print('Error reading data')
        print(e)
        return None
    else:
        return xml.getroot()
    
def get_currency_data():
    urlCur = 'http://www.cbr.ru/scripts/XML_val.asp?d=0'
    nodes = get_xmldoc(urlCur)
    if nodes:    
        # чтение списка валют и кодов в словарь dict_vals
        dict_vals = {}
        for child in nodes:
            id_val = child.attrib['ID']
            for x in child.iter('EngName'):   # Name attr - in russian
                val = x.text
            dict_vals[val] = id_val
        return dict_vals
    else:
        print('Cannot access data')
        #raise KeyboardInterrupt
        return None    

def get_rates(id_cur, start, end):    
    # получение котировок    
    urlDyn = f'https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={start}&date_req2={end}&VAL_NM_RQ={id_cur}'
    nodes2 = get_xmldoc(urlDyn)

    if nodes2:
        list_val = []
        for node in nodes2:
            for i in node.iter('Value'):
                list_val.append((node.attrib['Date'], float(i.text.replace(',','.'))) ) # list of tuples (date, value)
        return list_val

    else:
        print('Cannot access data')
        return None