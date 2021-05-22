#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        value = arr[i]
        hole = i

        while (hole > 0 and arr[hole-1] > value):
            arr[hole] = arr[hole-1]
            hole = hole-1

        arr[hole] = value
        print(*arr, sep=" ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
