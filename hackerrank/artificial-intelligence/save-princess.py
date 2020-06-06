#!/bin/python3

def build_grid(n):
    return [input() for _ in range(n)]

def display_path_to_princess(n, grid):
    if 'p' in grid[0]:
        princess = grid[0].index('p')
        line = 0
    elif 'p' in grid[n-1]:
        princess = grid[n-1].index('p')
        line = n-1
    
    hero = n // 2
    while hero != line:
        if hero > line:
            hero -= 1
            print('UP')
        else:
            hero += 1
            print('DOWN')
    
    hero = n // 2
    while hero != princess:
        if hero > princess:
            hero -= 1
            print('LEFT')
        else:
            hero += 1
            print('RIGHT')

def main():
    n = int(input().strip())
    grid = build_grid(n)

    display_path_to_princess(n, grid)

if __name__ == '__main__':
    main()
