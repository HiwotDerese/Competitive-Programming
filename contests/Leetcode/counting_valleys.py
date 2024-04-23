#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    sums = 0
    count = 0
    for i in range(steps):
        if i != 1:
            if path[i] == "U":
                sums = sums + 1
            elif path[i] == "D":
                sums = sums - 1
            if sums == 0:
                count = count + 1
                
        elif ((i == 1) and (path[i] == path[i+1])):
            if path[i] == "U":
                sums = sums + 1
            elif path[i] == "D":
                sums = sums - 1
            
        elif ((i == 1) and (path[i] != path[i+1])):
            if path[i] == "U":
                sums = sums + 1
            elif path[i] == "D":
                sums = sums - 1
            if sums == 0:
                count = count + 1
    return count
            
                
            
                

            
            
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
