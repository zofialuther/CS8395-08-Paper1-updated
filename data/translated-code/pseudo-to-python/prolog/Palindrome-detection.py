def palindrome(word):
    lst = list(word)
    reversed_lst = lst[::-1]
    return lst == reversed_lst