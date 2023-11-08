def digit_sum(N, Base, Sum):
    return digit_sum_helper(N, Base, Sum, 0)

def digit_sum_helper(N, Base, Sum, S1):
    if N < Base:
        return S1 + N
    else:
        M = N // Base
        Digit = N % Base
        S2 = S1 + Digit
        return digit_sum_helper(M, Base, Sum, S2)

def digital_root(N, Base, AP, DR):
    return digital_root_helper(N, Base, AP, DR, 0)

def digital_root_helper(N, Base, AP, DR, AP1):
    if N < Base:
        return AP, N
    else:
        Sum = digit_sum(N, Base)
        AP2 = AP1 + 1
        return digital_root_helper(Sum, Base, AP, DR, AP2)

def test_digital_root(N, Base):
    AP, DR = digital_root(N, Base, 0, 0)
    print(f'{N} has additive persistence {AP} and digital root {DR}.')

def main():
    test_digital_root(627615, 10)
    test_digital_root(39390, 10)
    test_digital_root(588225, 10)
    test_digital_root(393900588225, 10)
    test_digital_root(685943443231217865409, 10)

main()