#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    p = arr[0]
    left = []
    right = [] 
    
    for i in range(1, len(arr)):
        if arr[i] > p:
            right.append(arr[i])
        
        if arr[i] < p:
            left.append(arr[i])
            
    return left + [p] + right

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    print(*result, sep=" ")