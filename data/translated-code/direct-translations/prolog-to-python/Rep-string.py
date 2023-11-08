from func import *

def test_for_repstring(String):
    Reps = set(repstring(String))
    if Reps:
        return (String, 'repstrings', list(Reps))
    else:
        return (String, 'no repstring', [])

def repstring(Codes):
    Reps = set()
    for RepLength in range(1, len(Codes)//2 + 1):
        for i in range(len(Codes) - RepLength):
            R = Codes[i:i+RepLength]
            if Codes.startswith(R, i+RepLength):
                Reps.add(R)
    return Reps

def test_strings(strings):
    return [test_for_repstring(s) for s in strings]

def report_repstring(data):
    S, Result, Reps = data
    print(f'{S} -- {Result}: ', end='')
    for R in Reps:
        print(f'{R}, ', end='')
    print()

def report_repstrings():
    Results = map(test_for_repstring, test_strings([
        '1001110011', '1110111011', '0010010010', '1010101010',
        '1111111111', '0100101101', '0100100', '101', '11', '00', '1'
    ]))
    for R in Results:
        report_repstring(R)

report_repstrings()