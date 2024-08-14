#!/bin/python3

import os
import re

# Complete the solve function below.
def solve(s):
    # Use regex to find all words and capitalize them
    result = re.sub(r'\b\w', lambda x: x.group().upper(), s)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
