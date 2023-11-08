def is_palindrome(x):
    reversed_x = x[::-1]
    if x == reversed_x:
        return True
    else:
        return False