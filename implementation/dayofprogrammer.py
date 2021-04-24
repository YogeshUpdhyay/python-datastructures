#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, date
#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here

    def leapYear(year):
        if year > 1918:
            if (year % 400 == 0 or (year % 4 == 0 and year % 100)):
                return True
            return False
        else:
            if (year % 4 == 0):
                return True
            return False

    if year < 1918:
        if leapYear(year):
            return "12.09.{}".format(str(year))
        else:
            return "13.09.{}".format(str(year))
    elif year == 1918:
        return "26.09.1918"
    else:
        if leapYear(year):
            return "12.09.{}".format(str(year))
        else:
            return "13.09.{}".format(str(year))

        

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)
