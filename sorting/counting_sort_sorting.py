#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    freq = [0]*100
    for i in arr:
        freq[i] += 1
    
    sorted_arr = []
    for i in range(0,100):
        if freq[i] > 0:
          sorted_arr += [i]*freq[i]
    
    return sorted_arr

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(*result, sep=" ")
