def report_duplicates(S):
    dups = duplicates(S)
    print(f'For value "{S}":')
    report(dups)
    print()

def report(dups):
    if all(map(only_one_position, dups)):
        print('    All characters are unique')
    else:
        char, positions = next((c, positions) for c, positions in dups if len(positions) > 1)
        pos_in_order = ', '.join(map(str, reversed(positions)))
        print(f'    The character {char} is non unique at {pos_in_order}')

def only_one_position(char_positions):
    return len(char_positions[1]) == 1

def duplicates(S):
    chars = list(S)
    return char_count(chars, 0, [], [])

def char_count(chars, index, counted, result):
    if not chars:
        return result
    c = chars[0]
    if c in [char for char, _ in counted]:
        char_index = next(i for i, (char, _) in enumerate(counted) if char == c)
        counted[char_index][1].append(index + 1)
        return char_count(chars[1:], index + 1, counted, result)
    else:
        counted.append((c, [index + 1]))
        return char_count(chars[1:], index + 1, counted, result)

# Test cases
report_duplicates('')
report_duplicates('.')
report_duplicates('abcABC')
report_duplicates('XYZ ZYX')
report_duplicates('1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ')