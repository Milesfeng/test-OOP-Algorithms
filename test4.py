# -*- coding: utf-8 -*-

import numpy as np

# =============================================================================
# 正序排列
# =============================================================================

data = np.array([77,5,5,22,13,55,97,4,796,1,0,9])

def bubble_sort(data):
    for j in range(len(data)-1,0,-1):
        for i in range(j):
            if  data[i] > data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
    return data


