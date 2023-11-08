from enum import Enum
from random import randint

class Color(Enum):
    Red = 0
    White = 1
    Blue = 2

def dutch(colors):
    return sorted(colors)

def isDutch(colors):
    return colors == dutch(colors)

def randomBalls(n):
    if n == 0:
        return []
    else:
        return [Color(randint(0, 2)) for _ in range(n)]

def main():
    a = randomBalls(20)
    if isDutch(a):
        print("The random sequence", a, "is already in the order of the Dutch national flag!")
    else:
        print("The starting random sequence is", a)
        print("The ordered sequence is", dutch(a))

main()