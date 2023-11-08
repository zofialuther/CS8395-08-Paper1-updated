class MiddleThreeDigits:
    def middleThreeDigits(self, number):
        num_str = str(number)
        if len(num_str) < 3 or len(num_str) % 2 == 0:
            return "Number must be odd and have at least 3 digits"
        middle_index = len(num_str) // 2
        return num_str[middle_index-1:middle_index+2]

def main():
    mtd = MiddleThreeDigits()
    test_cases = [1234567, 987654321, 13579, 2468, 1234]
    for num in test_cases:
        result = mtd.middleThreeDigits(num)
        print(f"The middle three digits of {num} are {result}")

if __name__ == "__main__":
    main()