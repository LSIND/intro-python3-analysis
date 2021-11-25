#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

from deco_time import fdeco
import numpy as np

SIZE = 10000000

@fdeco
def zip_lists():
    L1 = range(SIZE)                    # lists L1 = L2 = [0,1,2,...,100000000]
    L2 = range(SIZE)
    result = [(x,y) for x,y in zip(L1,L2)]
    print(result[0:10])

@fdeco
def zip_numpy_arr():
    N1 = np.arange(SIZE) # NP Array N1 = N2 = [0,1,2,...,100000000]
    N2 = np.arange(SIZE)
    result = np.dstack((N1, N2))
    print(result[0][0:10])          # dimensions: 1 : SIZE : 2

if __name__ == '__main__':
    zip_lists()
    zip_numpy_arr()