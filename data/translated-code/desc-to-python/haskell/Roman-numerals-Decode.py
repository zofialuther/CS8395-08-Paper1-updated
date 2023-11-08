```python
def romanValue(roman_numeral):
    roman_numerals = [
        ("I", 1), ("V", 5), ("X", 10), ("L", 50), 
        ("C", 100), ("D", 500), ("M", 1000)
    ]
    result = 0
    for i in range(len(roman_numeral)):
        if i > 0 and roman_numerals.index((roman_numeral[i], 1)) > roman_numerals.index((roman_numeral[i-1], 1)):
            result += roman_numerals[roman_numerals.index((roman_numeral[i], 1))][1] - 2 * roman_numerals[roman_numerals.index((roman_numeral[i-1], 1))][1]
        else:
            result += roman_numerals[roman_numerals.index((roman_numeral[i], 1))][1]
    return result

def main():
    roman_numerals_list = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    for numeral in roman_numerals_list:
        print(romanValue(numeral))

main()
```