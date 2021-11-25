#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
'''reads currency rates from Central Bank of Russia (cbr.ru) in XML-format using module xml.etree.ElementTree'''

from urllib.request import urlopen
from xml.etree.ElementTree import parse
from datetime import datetime

def getInput(val, date1, date2):
    '''get id of the currency name'''
    id = readXML(val)
    if id is not None:
        return readVal(id, date1, date2)
    else:
        print("no currency found")

def readXML(val):
    '''finds VAL_NM_RQ by its name, f.e. Euro = R01239'''
    varurl = urlopen("http://www.cbr.ru/scripts/XML_val.asp?d=0")
    xml1 = parse(varurl)
    nodes = xml1.getroot()
    id = None

    for node in nodes:
        for i in list(node):
            if i.text == val:
                id = node.attrib['ID']
                print(id)
                break
    return id

def readVal(idval, date1, date2):
    ''' read rates of currency in a period'''
    startdate = datetime.strptime(date1,'%d.%m.%Y') 
    enddate = datetime.strptime(date2,'%d.%m.%Y') 

    varurl2 = urlopen("http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1="+date1+"&date_req2="+date2+"&VAL_NM_RQ="+idval)
    xml2 = parse(varurl2)
    nodes2 = xml2.getroot()

    listdates = []
    listval = []
    list1 = []

    for node in nodes2:
        listdates.append(datetime.strptime(node.attrib['Date'], '%d.%m.%Y'))
        list1.append(node.attrib['Date'])
        for i in node.iter('Value'):
            listval.append(float(i.text.replace(",",".")))
    return listdates, listval
