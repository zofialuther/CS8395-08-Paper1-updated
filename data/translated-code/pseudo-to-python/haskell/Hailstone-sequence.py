def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 1 + 3 * n

def hailstone(n):
    result = []
    while n != 1:
        result.append(n)
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 1 + 3 * n
    result.append(1)
    return result

def longestChain():
    maxChainLength = 0
    numberWithMaxChain = 0
    for i in range(1, 100000):
        chainLength = len(hailstone(i))
        if chainLength > maxChainLength:
            maxChainLength = chainLength
            numberWithMaxChain = i
    return numberWithMaxChain

def main():
    print("Collatz sequence for 27: ")
    print(hailstone(27))
    print("The number " + str(longestChain()) + " has the longest hailstone sequence for any number less than 100000.")
    print("The sequence has length: " + str(len(hailstone(longestChain()))) )