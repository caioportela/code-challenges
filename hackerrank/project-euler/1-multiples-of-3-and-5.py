#!/bin/python3

def series(n):
    return n * (n + 1) // 2

def multiples_sum(n):
    return (series(n // 3) * 3) + (series(n // 5) * 5) - (series(n // 15) * 15)

def main():
    t = int(input().strip())
    
    for _ in range(t):
        n = int(input().strip())

        result = multiples_sum(n-1)
        print(result)

if __name__ == '__main__':
    main()
