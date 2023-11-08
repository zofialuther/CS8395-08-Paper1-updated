class Roman:
    @staticmethod
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

    @staticmethod
    def decode(roman):
        result = 0
        uRoman = roman.upper()  # case-insensitive
        for i in range(len(uRoman) - 1):
            if Roman.decodeSingle(uRoman[i]) < Roman.decodeSingle(uRoman[i + 1]):
                result -= Roman.decodeSingle(uRoman[i])
            else:
                result += Roman.decodeSingle(uRoman[i])
        result += Roman.decodeSingle(uRoman[-1])
        return result

print(Roman.decode("MCMXC"))  # 1990
print(Roman.decode("MMVIII"))  # 2008
print(Roman.decode("MDCLXVI"))  # 1666