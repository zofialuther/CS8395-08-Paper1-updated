def combinations_of_length(_,[]):
    pass

def combinations_of_length(lst, combinations):
    if lst:
        combinations.append(lst[0])
        combinations_of_length(lst, combinations)
    else:
        combinations_of_length(lst[1:], combinations)

# Example usage
lst = [1, 2, 3]
combinations = []
combinations_of_length(lst, combinations)
print(combinations)