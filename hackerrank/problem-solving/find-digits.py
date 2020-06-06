#!/bin/python3

import os

def findDigits(n):
    n_str = str(n)
    count = 0

    for digit in set(n_str):
        if digit != '0' and n % int(digit) == 0:
            count += n_str.count(digit)

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
