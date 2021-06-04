#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    n = len(arr)
    
    mid = int(n/2)
    i = 0
    while i < mid:
        arr[i][1] = "-"
        i += 1
    
    freq = [[] for _ in range(len(arr))]
    
    for i in arr:
        freq[int(i[0])].append(i[1])
    
    temp = ""
    for i in freq:
        if len(i) > 0:
            temp += " ".join(i)
            temp+= " "
    
    print( temp )
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
