def spellInteger(number):
    small_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_numbers = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    big_numbers = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion", "quinquadecillion", "sedecillion", "septendecillion", "octodecillion", "novemdecillion", "vigintillion", "centillion"]

    if number < 0:
        return "negative " + spellInteger(-number)
    elif number < 20:
        return small_numbers[number]
    elif number < 100:
        return tens_numbers[number // 10] + (" " + small_numbers[number % 10] if (number % 10) != 0 else "")
    else:
        result = ""
        for i in range(len(big_numbers)):
            if number == 0:
                break
            if number % 1000 != 0:
                result = spellInteger(number % 1000) + " " + big_numbers[i] + (" " + result if result else "")
            number //= 1000
        return result.strip()