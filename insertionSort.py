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
    x = arr[n - 1]
    for i in range((n - 2), -1, -1):
        if x < arr[i]:
            arr[ i + 1] = arr[i]
            for i in arr:
                print(i,end=" ")
            print()
            
        else:
            arr[i + 1] = x
    
    for i in arr:
        print(i,end=" ")

    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
