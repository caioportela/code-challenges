#!/bin/python3

import math
import os
import random
import re
import sys

def climbingLeaderboard(scores, alice):
    rank = len(set(scores)) + 1
    last = len(scores) - 1
    result = []

    for points in alice:
        for i in range(last, -1, -1):
            last = i

            if points < scores[i]:
                result.append(rank)
                break
            
            if i == 0 and points >= scores[i]:
                result.append(1)
            elif i > 0 and scores[i] != scores[i-1]:
                rank -= 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
