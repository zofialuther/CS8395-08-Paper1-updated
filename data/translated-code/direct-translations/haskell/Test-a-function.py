import random
import string
import unittest

def isPalindrome(x):
    return x == x[::-1]

class TestIsPalindrome(unittest.TestCase):
    def test_even_palindromes(self):
        for _ in range(100):
            s = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(0, 10)))
            self.assertTrue(isPalindrome(s + s[::-1]))

    def test_odd_palindromes(self):
        for _ in range(100):
            s = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 10)))
            idx = random.randint(0, len(s) - 1)
            self.assertTrue(isPalindrome(s + s[:idx:-1]))

    def test_non_palindromes(self):
        for _ in range(100):
            s = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(0, 10)))
            idx = random.randint(0, len(s))
            if idx * 2 != len(s):
                self.assertFalse(isPalindrome(s[:idx] + '•' + s[idx:]))

if __name__ == '__main__':
    unittest.main()