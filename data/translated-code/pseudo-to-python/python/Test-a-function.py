def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def _test():
    import doctest
    doctest.testmod()
    #doctest.testmod(verbose=True)

if __name__ == "__main__":
    _test()