```python
# Import the necessary library
from pyswip import Prolog

# Create a Prolog object
prolog = Prolog()

# Assert the character types
prolog.assertz("char_type(a, lower)")
prolog.assertz("char_type(b, lower)")
prolog.assertz("char_type(A, upper)")
prolog.assertz("char_type(B, upper)")

# Query for all lower case characters
lower_case_chars = list(prolog.query("char_type(Char, lower)"))
print("Lower case characters:", [result["Char"] for result in lower_case_chars])

# Query for all upper case characters
upper_case_chars = list(prolog.query("char_type(Char, upper)"))
print("Upper case characters:", [result["Char"] for result in upper_case_chars])
```