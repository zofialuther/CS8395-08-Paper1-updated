def main():
    for N in range(1, 41):
        M = min_mult_dsum(N)
        print(f'{M:6}', end='')
        if N % 10 == 0:
            print()
    return


def min_mult_dsum(N, M=1):
    if M * N == digit_sum(M * N, N):
        return M
    else:
        return min_mult_dsum(N, M+1)


def digit_sum(N, Sum=0):
    if N < 10:
        return Sum + N
    else:
        M, Digit = divmod(N, 10)
        return digit_sum(M, Sum + Digit)


main()