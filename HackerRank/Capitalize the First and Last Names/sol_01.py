#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    names = s.split() # split string with spaces
    capitalizedName = [name.capitalize() for name in names] # Capitalize each part
    return ' '.join(capitalizedName) # join with space
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
