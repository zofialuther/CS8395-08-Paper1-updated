```python
import bisect
import sys

LOWER = 0
UPPER = 100

def main():
    print(f"Instructions:\n"
          f"Think of integer number from {LOWER} (inclusive) to {UPPER} (exclusive) and\n"
          f"I will guess it. After each guess, you respond with L, H, or C depending\n"
          f"on if my guess was too low, too high, or correct.\n")

    result = bisect.bisect_left([query(i) for i in range(UPPER - LOWER)], 0)
    if result < 0:
        print("That is impossible.")
    else:
        print(f"Your number is {result}.")

def query(i):
    print(f"My guess is: {LOWER + i}. Is it too high, too low, or correct? (H/L/C) ", end='')
    sys.stdout.flush()
    s = input().strip().lower()
    if s == 'l':
        return -1
    elif s == 'h':
        return 1
    elif s == 'c':
        return 0
    return -1

if __name__ == "__main__":
    main()
```