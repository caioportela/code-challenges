#!/bin/python3

import os

def jump(i, c, k):
    return (i + k) % len(c)

def consume(cloud):
    return (cloud * 2) + 1

def jumpingOnClouds(c, k):
    energy = 100

    i = jump(0, c, k)
    energy -= consume(c[i])
    
    while i > 0:
        i = jump(i, c, k)
        energy -= consume(c[i])

    return energy
    
def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nk = input().split()
    n = int(nk[0])  
    k = int(nk[1])
    
    c = list(map(int, input().rstrip().split()))
    
    result = jumpingOnClouds(c, k)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
        
if __name__ == '__main__':
    main()
