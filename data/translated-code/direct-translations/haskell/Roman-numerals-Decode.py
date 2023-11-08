from itertools import accumulate

def romanValue(s):
    roman_numerals = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4),
        ("I", 1)
    ]
    
    def tr(acc, x):
        k, v = x
        while s.startswith(k):
            s = s[len(k):]
            acc += v
        return (s, acc)

    return sum(accumulate(roman_numerals, tr, initial=(s, 0)))

def main():
    roman_numerals = ["MDCLXVI", "MCMXC", "MMVIII", "MMXVI", "MMXVII"]
    for numeral in roman_numerals:
        print(romanValue(numeral))

main()