class Kaprekar:
    def __init__(self, base):
        self.base = base

    def is_kaprekar(self, num):
        square = num ** 2
        square_str = str(square)
        for i in range(1, len(square_str)):
            left = int(square_str[:i])
            right = int(square_str[i:])
            if left + right == num and right != 0:
                return True
        return False

if __name__ == "__main__":
    import sys
    base = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    kaprekar = Kaprekar(base)
    for num in range(1, 1000000):
        if kaprekar.is_kaprekar(num):
            print(num)