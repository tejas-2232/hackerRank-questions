#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'solution' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER numLocations
#  2. 2D_INTEGER_ARRAY journey
#

def solution(numLocations, journey):
    # Write your code here

    color = [-1] * numLocations
    for i in range(numLocations):
        
        if color[i] == -1:
            queue = deque()
            queue.append(i)
            color[i] = 0
        
            while queue:
                current = queue.popleft()
                
                for neighbor in range(numLocations):
                    if journey[current][neighbor] == 1:
                        if color[neighbor] == -1:
                            color[neighbor] = color[current] ^ 1
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:
                            return False
    return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    numLocations = int(input().strip())
    journey = []
    for _ in range(numLocations):
        journey.append(list(map(int, input().rstrip().split())))
    ret = solution(numLocations, journey)
    fptr.write(str(int(ret)) + '\n')
    fptr.close()
