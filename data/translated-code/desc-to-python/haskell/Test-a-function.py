```python
import Test.QuickCheck

def is_palindrome(s):
    return s == s[::-1]

prop_even_length_palindrome(s):
    even_length_palindrome = s + s[::-1]
    return is_palindrome(even_length_palindrome)

prop_odd_length_palindrome(s):
    odd_length_palindrome = s + s[-2::-1]
    return is_palindrome(odd_length_palindrome)

prop_non_palindrome(s):
    return not is_palindrome(s)

instance Arbitrary Char where
  arbitrary = choose ('\32', '\128')

quickCheck prop_even_length_palindrome
quickCheck prop_odd_length_palindrome
quickCheck prop_non_palindrome
```