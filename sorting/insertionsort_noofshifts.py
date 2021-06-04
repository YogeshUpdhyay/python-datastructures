#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    shifts = 0
    for i in range(1, len(arr)):
        value = arr[i]
        hole = i

        while (hole > 0 and arr[hole-1] > value):
            shifts += 1
            arr[hole] = arr[hole-1]
            hole = hole-1

        arr[hole] = value
    return shifts
        
    
    
if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    print(result)