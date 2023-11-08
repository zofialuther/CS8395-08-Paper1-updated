def main():
    print_list(1, 10)

def print_list(Min, Max):
    if Min < Max:
        print(Min, end='')
        Min1 = Min + 1
        if Min % 5 == 0:
            print('\n', end='')
        else:
            print(',', end='')
        print_list(Min1, Max)
    else:
        print(Max)
        print('\n')

main()