def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Args:
    s (str): Input string to check for palindrome

    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    return s == s[::-1]

def _test():
    """
    Run doctests to verify the functionality of is_palindrome function.
    """
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("madam") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("apple") == False

if __name__ == "__main__":
    _test()