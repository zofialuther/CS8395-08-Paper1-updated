def search_a_list(N1, N2):
    L = ["Zig", "Zag", "Wally", "Ronald", "Bush", "Krusty", "Charlie", "Bush", "Boz", "Zag"]
    print('List is :')
    list(map(my_write, L))
    print('\n\n')

    if N1 in L:
        print('%s is in position %d' % (N1, L.index(N1)))
    else:
        print('%s is not present' % N1)

    if N2 in L:
        print('%s is in position %d' % (N2, L.index(N2)))
    else:
        print('%s is not present' % N2)

    if N1 in L:
        print('%s last position is %d' % (N1, len(L) - L[::-1].index(N1) - 1))
    else:
        print('%s is not present' % N1)


def reverse_nth1(Ind, L, N):
    RL = L[::-1]
    Len = len(L)
    Ind1 = RL.index(N)
    Ind = Len - Ind1 + 1


def my_write(Name):
    print(' %s' % Name)