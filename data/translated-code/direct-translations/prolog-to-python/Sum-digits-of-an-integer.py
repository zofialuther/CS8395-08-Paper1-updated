def digit_sum(N, Base, Sum):
    digit_sum_helper(N, Base, Sum, 0)

def digit_sum_helper(N, Base, Sum, S1):
    if N < Base:
        Sum = S1 + N
    else:
        M = N // Base
        Digit = N % Base
        S2 = S1 + Digit
        digit_sum_helper(M, Base, Sum, S2)

def test_digit_sum(N, Base):
    Sum = 0
    digit_sum(N, Base, Sum)
    print(f"Sum of digits of {N} in base {Base} is {Sum}.")

def main():
    test_digit_sum(1, 10)
    test_digit_sum(1234, 10)
    test_digit_sum(0xfe, 16)
    test_digit_sum(0xf0e, 16)

main()