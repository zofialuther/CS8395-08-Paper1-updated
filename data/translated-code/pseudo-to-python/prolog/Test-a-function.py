def palindrome(Word):
    List = list(Word)
    Reversed = List[::-1]
    if List == Reversed:
        return True
    else:
        return False

# Testing
assert palindrome('ingirumimusnocteetconsumimurigni') == True
assert palindrome('this is not a palindrome') == False