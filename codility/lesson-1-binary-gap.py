MAX_NUMBER = 2147483647

def solution(N):
    # Just run some checks before get started
    if not isinstance(N, int):
        raise TypeError('Input must be integer')

    if N < 1:
        raise TypeError('Input must be positivist')

    if N > MAX_NUMBER:
        raise TypeError('Input must be cool')


    number_binary = str(bin(N))[2:]  # Convert number to binary

    longest = None  # Tracks the longest binary gap
    was_zero = None  # Tracks if the last bit was zero
    count = 0  # Tracks the number of zeros in the sequence

    for bit in number_binary:
        is_zero = bit == '0'

        if bool(was_zero) != bool(is_zero):
            if longest is None:
                longest = 0
            elif count > longest:
                longest = count

            count = 1
        else:
            count += 1

        was_zero = is_zero

    if longest is not None:
        return longest

    return 0

if __name__ == '__main__':
    solution(0)
