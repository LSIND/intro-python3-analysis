#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

''' decorator: time of execution '''
import time

def fdeco(func):
    '''decorator: time of execution'''
    def wrapfunc(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        print(f'Time of {func.__name__} : {end - start} ms')
        print('-'*10)
        return res
    return wrapfunc