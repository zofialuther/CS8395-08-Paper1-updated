from functools import cmp_to_key

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 1 + 3 * n

def hailstone(n):
    sequence = [n]
    while n != 1:
        n = collatz(n)
        sequence.append(n)
    return sequence

def longestChain():
    max_length = 0
    max_num = 0
    for i in range(1, 100001):
        length = len(hailstone(i))
        if length > max_length:
            max_length = length
            max_num = i
    return max_num

def main():
    print("Collatz sequence for 27: ", hailstone(27))
    longest = longestChain()
    print(f"The number {longest} has the longest hailstone sequence for any number less than 100000.")
    print("The sequence has length: ", len(hailstone(longest)))

if __name__ == "__main__":
    main()