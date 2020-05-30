#!/bin/python3

import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    word = [h[ord(char)-97] for char in word]
    return max(word) * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
