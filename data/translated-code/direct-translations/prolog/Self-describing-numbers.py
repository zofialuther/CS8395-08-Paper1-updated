import itertools

from prologterms import TermGenerator

tg = TermGenerator()

# search of the self_describling numbers of a given len
def self_describling(Len, N):
    L = [tg.var() for _ in range(Len)]
    Len1 = Len - 1

    H = L[0]
    T = L[1:]

    # the first figure is greater than 0
    H.in_set(range(1, Len1 + 1))

    # there is at least two figures so the number of these figures
    # is at most Len - 2
    Len2 = Len - 2
    for t in T:
        t.in_set(range(Len2 + 1))

    # the sum of the figures is equal to the len of the number
    sum(L, N)

    # There is at least one figure corresponding to the number of zeros
    H1 = H + 1
    V = L[H1 - 1]
    V > 0

    # create the list
    label(L)

    # test the list
    LNS = sorted(L)
    LNP = packList(LNS)
    NumList = list(range(Len1 + 1))
    verif(LNP, NumList, L)

    # list is OK, create the number
    N = int(''.join(map(str, L)))


def packList(L):
    if not L:
        return []
    if len(L) == 1:
        return [[1, L[0]]]

    packed = []
    i = 0
    while i < len(L):
        count = 1
        j = i + 1
        while j < len(L) and L[j] == L[i]:
            count += 1
            j += 1
        packed.append([count, L[i]])
        i = j

    return packed


def verif(PackList, Order_of_Numeral, Numeral_of_the_number_to_test):
    if not PackList and not Order_of_Numeral and not Numeral_of_the_number_to_test:
        return True
    if not PackList and all(num == 0 for num in Numeral_of_the_number_to_test):
        return True
    if PackList and Order_of_Numeral and Numeral_of_the_number_to_test:
        V, N = PackList[0]
        if N == Order_of_Numeral[0]:
            return verif(PackList[1:], Order_of_Numeral[1:], Numeral_of_the_number_to_test[1:])
        if N == 0 and Order_of_Numeral[0] < N:
            return verif(PackList, Order_of_Numeral[1:], Numeral_of_the_number_to_test[1:])
    return False


def main():
    for I in range(1, 11):
        L = [self_describling(I, N) for N in range(1, 11)]
        print(f"Len {I}, Numbers {L}")


if __name__ == "__main__":
    main()