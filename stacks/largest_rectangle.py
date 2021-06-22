# Largest Recatangle Problems

# Given an array of heights of buildings( equivalent to histogram) find the largest
# rectangle.

# Ex input : [1, 2 ,3, 4, 5]
# Answer 9


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    max_area = 0
    i = 0
    while i < len(h):

        count = 1

        j = i-1
        while j >= 0:
            if h[j] >= h[i]:
                count += 1
                j -= 1
            else:
                break

        k = i+1
        while k < len(h):
            if h[k] >= h[i]:
                count += 1
                k += 1
            else:
                break

        max_area = max(max_area, count*h[i])

        i+=1
    
    return max_area
        
        

if __name__ == '__main__':

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(result)