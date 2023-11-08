import random
t = random.randint(1, 10)
g = 0

while g != t:
    g = int(input("Enter your guess for a number between 1 and 10: "))
    
print("That's right!")