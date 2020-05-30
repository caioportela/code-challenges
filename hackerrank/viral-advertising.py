#!/bin/python3

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    share = 5
    likes = 0
    
    for day in range(n):
        half = share // 2
        likes += half
        share = half * 3

    return likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
