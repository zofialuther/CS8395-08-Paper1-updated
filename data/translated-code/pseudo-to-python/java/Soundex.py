def main(args):
    print(soundex("Soundex"))
    print(soundex("Example"))
    print(soundex("Sownteks"))
    print(soundex("Ekzampul"))

def getCode(c):
    switch = {
        'B': '1',
        'F': '1',
        'P': '1',
        'V': '1',
        'C': '2',
        'G': '2',
        'J': '2',
        'K': '2',
        'Q': '2',
        'S': '2',
        'X': '2',
        'Z': '2',
        'D': '3',
        'T': '3',
        'L': '4',
        'M': '5',
        'N': '5',
        'R': '6'
    }
    return switch.get(c, "")

def soundex(s):
    code = s.upper()[0]
    previous = getCode(s.upper()[0])
    
    for i in range(1, len(s)):
        current = getCode(s.upper()[i])
        if len(current) > 0 and current != previous:
            code += current
        previous = current
    
    soundex = (code + "0000")[:4]
    return soundex