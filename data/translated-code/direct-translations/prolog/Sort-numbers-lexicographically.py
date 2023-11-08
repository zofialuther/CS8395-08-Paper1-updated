def lexicographical_sort(Numbers, Sorted_numbers):
    Strings = [str(num) for num in Numbers]
    Sorted_strings = sorted(Strings)
    Sorted_numbers = [int(string) for string in Sorted_strings]

def number_strings(Numbers, Strings):
    if not Numbers:
        return []
    else:
        return [str(num) for num in Numbers]

def number_list(From, To):
    if From > To:
        return []
    else:
        return list(range(From, To+1))

def lex_sorted_number_list(Number):
    if Number < 1:
        Numbers = number_list(Number, 1)
    else:
        Numbers = number_list(1, Number)
    return lexicographical_sort(Numbers, List)

def test(Number):
    List = lex_sorted_number_list(Number)
    print(f'{Number}: {List}')

def main():
    test(0)
    test(5)
    test(13)
    test(21)
    test(-22)

main()