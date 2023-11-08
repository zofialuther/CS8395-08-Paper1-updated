```python
import random
import string

def generate_password(length, use_readable_chars):
    if use_readable_chars:
        characters = 'abcdefghjkmnpqrstuvwxyz23456789'
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def main(num_passwords, length, use_readable_chars):
    passwords = [generate_password(length, use_readable_chars) for _ in range(num_passwords)]
    for password in passwords:
        print(password)

main(5, 10, True)
```