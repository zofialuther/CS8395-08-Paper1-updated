def number_to_ordinal(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return str(num) + suffix

def spell_out_number(num):
    ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    if num == 0:
        return 'zero'
    elif num < 0:
        return 'negative ' + spell_out_number(abs(num))
    elif num < 10:
        return ones[num-1]
    elif num < 20:
        return teens[num-11]
    elif num < 100:
        return tens[(num//10)-1] + ('' if num%10 == 0 else '-' + ones[num%10-1])
    elif num < 1000:
        return ones[(num//100)-1] + ' hundred' + (' and ' + spell_out_number(num%100) if num%100 != 0 else '')
    else:
        return 'number is too large to spell out'

def test_ordinal_conversion():
    print(number_to_ordinal(1))  # first
    print(number_to_ordinal(2))  # second
    print(number_to_ordinal(3))  # third
    print(number_to_ordinal(4))  # fourth
    print(number_to_ordinal(11))  # eleventh