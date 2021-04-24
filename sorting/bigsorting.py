#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

# design a class with treats string as integer and replace the integers methods 
# with comparision dunder methods 
class StringAsInt(object):
    def __init__(self, obj, *args):
        self.obj = obj
    def __lt__(self, other):
        if len(self.obj) != len(other.obj):
            return len(self.obj) < len(other.obj)
        else:
            return self.obj < other.obj
    def __gt__(self, other):
        return other < self
    def __eq__(self, other):
        return self.obj == other.obj
    def __le__(self, other):
        return not (self > other)
    def __ge__(self, other):
        return (other <= self)
    def __ne__(self, other):
        return self.obj != other.obj

def bigSorting(unsorted):
    # Write your code here
    sortarr = sorted(unsorted, key=StringAsInt)
    return sortarr

if __name__ == '__main__':
    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)
    print(result)
