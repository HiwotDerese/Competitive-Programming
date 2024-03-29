#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    _minm = arr[-1]
    idx = n - 2
    while (_minm < arr[idx]) and (idx >= 0):
        arr[idx + 1] = arr[idx]
        print(*arr)
        idx -= 1

    arr[idx+1] = _minm
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
