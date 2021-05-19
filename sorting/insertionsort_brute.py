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
    temp = arr[-1]
    i = n-2
    while i >= 0:
        if arr[i] >= temp:
            arr[i+1] = arr[i]
            print(*arr, sep=" ")
        else:
            arr[i+1] = temp
            print(*arr, sep=" ")
            break

        i-=1

    if i == -1:
        arr[0] = temp
        print(*arr, sep=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
