from random import Random
import random
import string

class PasswordGenerator:
    rand = Random()

    @staticmethod
    def main(args):
        num = int(args[0])
        len = int(args[1])
        try:
            if len(args) != 2:
                raise ValueError
            if len < 4 or len > 16:
                raise ValueError
            if num < 1 or num > 10:
                raise ValueError
            for password in PasswordGenerator.generatePasswords(num, len):
                print(password)
        except ValueError:
            print("Please provide a valid length and number of passwords")

    @staticmethod
    def generatePasswords(num, len):
        s = string.punctuation
        result = []
        for _ in range(num):
            sb = PasswordGenerator.generatePasswordHelper(s, len)
            result.append(sb)
        return result

    @staticmethod
    def generatePasswordHelper(s, len):
        sb = random.choice(s) + random.choice(string.digits) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase)
        for _ in range(4, len):
            sb += random.choice(s.translate({ord(c): None for c in '\\`'}))
        return PasswordGenerator.shuffle(sb)

    @staticmethod
    def shuffle(sb):
        shuffled = list(sb)
        for i in range(len(shuffled)):
            j = PasswordGenerator.rand.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return ''.join(shuffled)