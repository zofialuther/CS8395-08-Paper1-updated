import random

def generate_password(length, quantity):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    for i in range(quantity):
        password = ''.join(random.choice(characters) for i in range(length))
        print(password)

generate_password(8, 5)