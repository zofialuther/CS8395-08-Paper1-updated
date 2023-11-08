def substring_task(Str, N, M, Char, SubStr):
    # Extract substring from index N to M
    result1 = Str[N:N+M]
    
    # Extract substring from index N to the end of the string
    result2 = Str[N:]
    
    # Extract string without the last character
    result3 = Str[:-1]
    
    # Extract substring from known character to index M
    result4 = Str[Str.index(Char):M]

    # Print the results of each operation
    print(result1)
    print(result2)
    print(result3)
    print(result4)

def string_from_substring_to_m(Str, N, M):
    return Str[N:M]