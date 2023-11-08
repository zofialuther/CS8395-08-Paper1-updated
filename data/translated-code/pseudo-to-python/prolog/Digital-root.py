def digit_sum(N, Base, Sum):
    return digit_sum_helper(N, Base, Sum, 0)

def digit_sum_helper(N, Base, Sum, S1):
    if N < Base:
        return Sum + S1 + N
    else:
        M, Digit = divmod(N, Base)
        S2 = S1 + Digit
        return digit_sum_helper(M, Base, Sum, S2)

def digital_root(N, Base, AP, DR):
    return digital_root_helper(N, Base, AP, DR, 0)

def digital_root_helper(N, Base, AP, DR, AP):
    if N < Base:
        return
    else:
        Sum = digit_sum(N, Base, 0)
        AP2 = AP + 1
        return digital_root_helper(Sum, Base, AP, DR, AP2)

def test_digital_root(N, Base):
    AP = 0
    DR = 0
    digital_root(N, Base, AP, DR)
    print(str(N) + " has additive persistence " + str(AP) + " and digital root " + str(DR))

def main():
    test_digital_root(627615, 10)
    test_digital_root(39390, 10)
    test_digital_root(588225, 10)
    test_digital_root(393900588225, 10)
    test_digital_root(685943443231217865409, 10)

main()