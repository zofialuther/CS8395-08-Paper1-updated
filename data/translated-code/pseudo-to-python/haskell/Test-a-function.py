from Test.QuickCheck import *

def isPalindrome(x):
    return x == x[::-1]

instance Arbitrary Char where
    arbitrary = choose('\32', '\127')

def main():
    print("Even palindromes: ")
    quickCheck(lambda s: isPalindrome(s + s[::-1]))
    print("Odd palindromes: ")
    quickCheck(lambda s: not (len(s) == 0) and isPalindrome(s + s[::-1][1:]))
    print("Non-palindromes: ")
    quickCheck(lambda i, s: not (len(s) == 0) and 0 <= i < len(s) and i*2 != len(s) and not isPalindrome(s[:i] + "•" + s[i:]))