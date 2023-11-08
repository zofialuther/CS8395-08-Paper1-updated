```python
import string

# Generate list of uppercase letters
uppercase_letters = list(filter(lambda x: x.isupper(), string.ascii_letters))

# Generate list of lowercase letters
lowercase_letters = list(filter(lambda x: x.islower(), string.ascii_letters))

# Format and print uppercase letters in chunks of 70 characters
for i in range(0, len(uppercase_letters), 70):
    print(''.join(uppercase_letters[i:i+70]))

# Format and print lowercase letters in chunks of 70 characters
for i in range(0, len(lowercase_letters), 70):
    print(''.join(lowercase_letters[i:i+70]))
```