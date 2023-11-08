def palindrome(Word):
    List = list(Word)
    return List == List[::-1]
    
import unittest

class TestPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertTrue(palindrome('ingirumimusnocteetconsumimurigni'))
        
    def test_invalid_palindrome(self):
        self.assertFalse(palindrome('this is not a palindrome'))

if __name__ == '__main__':
    unittest.main()