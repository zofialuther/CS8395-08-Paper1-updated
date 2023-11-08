from functools import partial

def binaryDigits(n):
    def go(n):
        if n == 0:
            return None
        else:
            return (str("01"[n % 2]), n // 2)
    return ''.join(unfoldr(go, n)[::-1])

def main():
    test_numbers = [5, 50, 9000]
    for number in test_numbers:
        print(str(number) + " -> " + binaryDigits(number))

main()