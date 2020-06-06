#!/bin/python3

def build_grid(n):
    return [input() for _ in range(n)]

def locate(grid):
    for l in grid:
        if 'p' in l:
            princess = l.index('p')
            row = grid.index(l)
            
            return princess, row

def main():
    n = int(input())
    bot = [int(i) for i in input().split()]
    grid = build_grid(n)
    
    princess, row = locate(grid)

    if bot[0] > row:
        print('UP')
    elif bot[0] < row:
        print('DOWN')
    elif bot[1] > princess:
        print('LEFT')
    elif bot[1] < princess:
        print('RIGHT')
    
if __name__ == '__main__':
    main()
