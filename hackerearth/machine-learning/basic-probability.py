def probability(pmb, pab, p1):
    return p1 * ((pmb * (1 - pab) + pab * (1 - pmb)))

def main():
    pmb = float(input())
    pab = float(input())
    p1 = float(input())

    p = probability(pmb, pab, p1)

    print('{:f}'.format(p))

if __name__ == '__main__':
    main()
