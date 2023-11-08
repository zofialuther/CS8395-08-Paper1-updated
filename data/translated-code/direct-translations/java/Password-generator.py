import random

def generate_passwords(num, length):
    s = "!\"#$%&'()*+,-./:;<=>?@[]^_{|}~"
    result = []

    for i in range(num):
        pw = random.choice(s) + str(random.randint(0, 9)) + random.choice('abcdefghijklmnopqrstuvwxyz') + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
        for j in range(4, length):
            r = chr(random.randint(33, 126))
            if r == '\\' or r == '`':
                j -= 1
            else:
                pw += r
        
        result.append(''.join(random.sample(pw, len(pw))))
    
    return result

def main():
    try:
        args = input("Enter length of passwords and number of passwords: ").split()
        if len(args) != 2:
            raise ValueError
        
        length = int(args[0])
        if length < 4 or length > 16:
            raise ValueError
        
        num = int(args[1])
        if num < 1 or num > 10:
            raise ValueError
        
        passwords = generate_passwords(num, length)
        for pw in passwords:
            print(pw)
    
    except ValueError:
        print("Provide the length of the passwords (min 4, max 16) you want to generate, and how many (min 1, max 10)")

if __name__ == "__main__":
    main()