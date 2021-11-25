#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import time

# decorator: time of execution
def fdeco(func):
    '''decorator: time of execution'''
    def wrapfunc():
        start = time.time()
        func()
        end = time.time()
        print(func.__name__) 
        print("Time of merging : ", end - start)
        print('-'*10)
    return wrapfunc