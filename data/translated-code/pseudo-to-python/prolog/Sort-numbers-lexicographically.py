def lexicographical_sort(Numbers, Sorted_numbers):
    Strings = []
    for num in Numbers:
        Strings.append(str(num))
    Sorted_strings = sorted(Strings)
    Sorted_numbers.clear()
    for s in Sorted_strings:
        Sorted_numbers.append(int(s))

def number_strings(Numbers, Strings):
    pass

def number_list(From, To, result):
    if From > To:
        return result
    result.append(From)
    return number_list(From + 1, To, result)

def lex_sorted_number_list(Number, List):
    if Number < 1:
        Numbers = number_list(Number, 1, [])
    else:
        Numbers = number_list(1, Number, [])
    lexicographical_sort(Numbers, List)

def test(Number):
    List = []
    lex_sorted_number_list(Number, List)
    print(f'{Number}: {List}')

def main():
    test(0)
    test(5)
    test(13)
    test(21)
    test(-22)

main()