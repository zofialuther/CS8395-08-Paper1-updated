```python
import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = '!"#$%&\'()*+,-./:;<=>?@[]^_{|}~'

allowed = lowercase + uppercase + digits + punctuation

visually_similar = 'Il1O05S2Z'


def new_password(length: int, readable=True) -> str:
    if length < 4:
        print("password length={} is too short,".format(length),
            "minimum length=4")
        return ''
    choice = random.SystemRandom().choice
    while True:
        password_chars = [
            choice(lowercase),
            choice(uppercase),
            choice(digits),
            choice(punctuation)
            ] + random.sample(allowed, length-4)
        if (not readable or
                all(c not in visually_similar for c in password_chars)):
            random.SystemRandom().shuffle(password_chars)
            return ''.join(password_chars)


def password_generator(length, qty=1, readable=True):
    for i in range(qty):
        print(new_password(length, readable))
```