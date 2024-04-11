#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import numpy as np
from deco_time import fdeco

@fdeco
def create_lists(size):
    list1 = list(range(size))       # lists L1 = L2 = [0,1,2,..,N-1]
    list2 = list(range(size))
    return list1, list2

@fdeco
def zip_lists(l1, l2):
    result = [(x,y) for x,y in zip(l1, l2)]
    #print(result[0:10])

@fdeco
def create_numpy_arrays(size):
    np1 = np.arange(size)  # NP Array N1 = N2 = [0,1,2,...,N]
    np2 = np.arange(size)
    return np1, np1

@fdeco
def zip_numpy_arr(np1, np2):
    result = np.dstack((np1, np2))
    #print(result[0][0:10])          # dimensions: 1 : SIZE : 2

if __name__ == '__main__':
    SIZE = 100000000   # size of array
    # create arrays
    l1, l2= create_lists(SIZE)
    n1, n2 = create_numpy_arrays(SIZE)    
    
    zip_lists(l1, l2)
    zip_numpy_arr(n1, n2)