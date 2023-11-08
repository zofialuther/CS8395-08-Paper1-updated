def decode_string(roman_numeral):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_value = 0
    for i in range(len(roman_numeral)):
        if i > 0 and roman_numerals[roman_numeral[i]] > roman_numerals[roman_numeral[i - 1]]:
            decimal_value += roman_numerals[roman_numeral[i]] - 2 * roman_numerals[roman_numeral[i - 1]]
        else:
            decimal_value += roman_numerals[roman_numeral[i]]
    return decimal_value

def test_decode_string():
    assert decode_string('III') == 3
    assert decode_string('IV') == 4
    assert decode_string('IX') == 9
    assert decode_string('LVIII') == 58
    assert decode_string('MCMXCIV') == 1994
    print("All tests pass!")

test_decode_string()