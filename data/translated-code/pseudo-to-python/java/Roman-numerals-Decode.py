def decodeSingle(letter):
    if letter == 'M':
        return 1000
    elif letter == 'D':
        return 500
    elif letter == 'C':
        return 100
    elif letter == 'L':
        return 50
    elif letter == 'X':
        return 10
    elif letter == 'V':
        return 5
    elif letter == 'I':
        return 1
    else:
        return 0

def decode(roman):
    result = 0
    uRoman = roman.upper()
    for i in range(len(uRoman) - 1):
        if decodeSingle(uRoman[i]) < decodeSingle(uRoman[i+1]):
            result -= decodeSingle(uRoman[i])
        else:
            result += decodeSingle(uRoman[i])
    result += decodeSingle(uRoman[-1])
    return result

def main():
    print(decode("MCMXC")) #1990
    print(decode("MMVIII")) #2008
    print(decode("MDCLXVI")) #1666