from enum import Enum
import random

class Color(Enum):
    Red = 1
    White = 2
    Blue = 3

def dutch(colors):
    return sorted(colors)

def isDutch(colors):
    return colors == dutch(colors)

def randomBalls(n):
    return [Color(random.randint(1, 3)) for _ in range(n)]

def main():
    a = randomBalls(20)
    if isDutch(a):
        print("The random sequence " + str(a) + " is already in the order of the Dutch national flag!")
    else:
        print("The starting random sequence is " + str(a) + "\n")
        print("The ordered sequence is " + str(dutch(a)))

if __name__ == "__main__":
    main()