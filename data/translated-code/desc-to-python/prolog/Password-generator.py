import random
import string
import argparse

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = random.choice(lowercase) + random.choice(uppercase) + random.choice(digits) + random.choice(special_characters)
    password += ''.join(random.choice(lowercase + uppercase + digits + special_characters) for _ in range(length - 4)

    return ''.join(random.sample(password, len(password)))

def main():
    parser = argparse.ArgumentParser(description='Generate random passwords')
    parser.add_argument('-l', '--length', type=int, default=8, help='Length of the passwords')
    parser.add_argument('-n', '--number', type=int, default=1, help='Number of passwords to generate')
    args = parser.parse_args()

    for _ in range(args.number):
        print(generate_password(args.length))

if __name__ == '__main__':
    main()