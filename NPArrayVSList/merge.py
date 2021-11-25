#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from deco_time import fdeco
import numpy as np
import array

SIZE = 10000000

@fdeco
def mergelists():
    L1 = [*range(SIZE)]         # lists L1 = L2 = [0,1,2,3,....,100000000]
    L2 = [*range(SIZE)]
    res = L1 + L2
    print(res[0:10])

@fdeco
def merge_arrays():
    A1 = array.array('i', range(SIZE))  # array from array module A1 = A2 = [0,1,2,...,100000000]
    A2 = array.array('i', range(SIZE))
    result = A1+A2 # merge two arrays
    print(result[0:10])


@fdeco
def merge_numpy_arr():
    N1 = np.arange(SIZE) # NP Array N1 = N2 = [0,1,2,...,100000000]
    N2 = np.arange(SIZE)
    result = np.append(N1, N2)   # merge two numpy arrays
    print(result[0:10])          # dimensions: 1 : SIZE : 2

if __name__ == '__main__':
    merge_lists()
    merge_arrays()
    merge_numpy_arr()
