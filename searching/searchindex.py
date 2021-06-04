#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#

def introTutorial(V, arr):
    # Write your code here
    mid = int(len(arr)/2)
    
    if arr[mid] == V:
        return mid
        
    if arr[mid] > V:
        return introTutorial(V, arr[:mid]) 
    else:
        return mid+1+introTutorial(V, arr[mid+1:])
        
if __name__ == '__main__':

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    print(result)
