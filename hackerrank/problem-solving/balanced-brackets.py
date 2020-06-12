#!/bin/python3

import os

def isBalanced(brackets):
    stack = []

    for bracket in brackets:
        if bracket in ['{', '[', '(']:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return 'NO'

            last = stack.pop()

            isCurly = bracket == '}' and last != '{'
            isParenthesis = bracket == ')' and last != '('
            isSquare = bracket == ']' and last != '['

            if isCurly or isParenthesis or isSquare:
                return 'NO'
    
    if len(stack) != 0:
        return 'NO'
    
    return 'YES'

def main():
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        t = int(input())

        for t_itr in range(t):
            s = input()

            result = isBalanced(s)

            fptr.write(result + '\n')

if __name__ == '__main__':
    main()
