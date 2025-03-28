#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'conversation_stack' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY mathew
#  2. STRING_ARRAY stephanie
#

def conversation_stack(mathew, stephanie):
    # mathew and stephanie have already been converted into lists of strings for your convenience
    mathew_reversed = mathew[::-1]
    stephanie_reversed = stephanie[::-1]
    
    result = []

    #take max between two

    max_len = max(len(mathew_reversed), len(stephanie_reversed))
    
    for i in range(max_len):
        if i < len(mathew_reversed):
            result.append(mathew_reversed[i])
        if i < len(stephanie_reversed):
            result.append(stephanie_reversed[i])
    return ' '.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    y = int(input().strip())

    mathew = input().rstrip().split()

    stephanie = input().rstrip().split()

    result = conversation_stack(mathew, stephanie)

    fptr.write(result + '\n')

    fptr.close()
