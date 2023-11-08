import random
import string

def generate_secure_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(random.choice(characters) for i in range(length))
    return secure_password

def generate_multiple_secure_passwords(num_passwords, length):
    return [generate_secure_password(length) for _ in range(num_passwords)]