#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    result = 0

    for i in a:
        current_count = a.count(i)
        diff_count = a.count(i-1)

        count = current_count + diff_count
        if count > result:
            result = count

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
