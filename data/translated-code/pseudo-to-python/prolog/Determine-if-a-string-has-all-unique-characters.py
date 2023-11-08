def report_duplicates(S):
    Dups = []
    duplicates(S, Dups)
    print('For value "' + S + '":\n')
    report(Dups)
    print('\n')

def report(Dups):
    if all_characters_unique(Dups):
        print('    All characters are unique\n')
    else:
        nonUniqueChar = find_non_unique_character(Dups)
        char = nonUniqueChar[0]
        positions = nonUniqueChar[1]
        print('    The character ' + char + ' is non unique at ' + ', '.join(map(str, positions)) + '\n')

def all_characters_unique(Dups):
    for i in range(len(Dups)):
        if len(Dups[i][1]) > 1:
            return False
    return True

def find_non_unique_character(Dups):
    for i in range(len(Dups)):
        if len(Dups[i][1]) > 1:
            return Dups[i]

def duplicates(S, Count):
    Chars = list(S)
    char_count(Chars, 0, [], Count)

def char_count(Chars, Index, Counted, Result):
    if Index == len(Chars):
        Result.extend(Counted)
    else:
        C = Chars[Index]
        charIndex = findCharIndex(C, Counted)
        if charIndex != -1:
            Counted[charIndex][1].append(Index)
        else:
            Counted.append([C, [Index]])
        char_count(Chars, Index + 1, Counted, Result)

def findCharIndex(C, Counted):
    for i in range(len(Counted)):
        if Counted[i][0] == C:
            return i
    return -1

report_duplicates('')
report_duplicates('.')
report_duplicates('abcABC')
report_duplicates('XYZ ZYX')
report_duplicates('1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ')