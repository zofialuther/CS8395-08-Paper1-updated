def is_palindrome(s):
    return s == s[::-1]

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()