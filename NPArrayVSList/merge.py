#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import array
from deco_time import fdeco
import numpy as np

@fdeco
def create_lists(size):
    list1 = list(range(size))       # lists L1 = L2 = [0,1,2,..,N-1]
    list2 = list(range(size))
    return list1, list2

@fdeco
def merge_lists(l1, l2):
    result = l1 + l2  # [0,1,2, ..N-1, 0,1,2 ...,N-1]
    return result

@fdeco
def create_arrays(size):
    arr1 = array.array('i', range(size))  # array from array lib A1 = A2 = [0,1,2, ..N-1]
    arr2 = array.array('i', range(size))
    return arr1, arr2

@fdeco
def merge_arrays(a1,a2):
    result = a1+a2 # merge two arrays [0,1,2, ..N-1, 0,1,2 ...,N-1]
    return result

@fdeco
def create_numpy_arrays(size):
    np1 = np.arange(size)  # NP Array N1 = N2 = [0,1,2,...,N]
    np2 = np.arange(size)
    return np1, np1

@fdeco
def merge_numpy_arrays(np1, np2):
    result = np.append(np1, np2)   # merge two numpy arrays
    return result          # dimensions: 1 

if __name__ == '__main__':
    SIZE = 10000000   # size of array

    # create arrays
    l1, l2= create_lists(SIZE)
    a1, a2 = create_arrays(SIZE)
    n1, n2 = create_numpy_arrays(SIZE)    

    # merge arrays
    list_res = merge_lists(l1, l2)
    arr_res = merge_arrays(a1, a2)
    np_array_res = merge_numpy_arrays(n1, n2)