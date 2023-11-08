```python
def minimum_abbreviation_length(Day_names, Min_length):
    Sorted_names = sorted(Day_names)
    minimum_abbreviation_length_helper(Sorted_names, Min_length, 1)

def minimum_abbreviation_length_helper(names, Min_length, M1):
    if len(names) == 1:
        return Min_length
    else:
        Name1, Name2, *Rest = names
        Length = common_prefix_length(Name1, Name2)
        M2 = max(M1, Length + 1)
        return minimum_abbreviation_length_helper([Name2] + Rest, Min_length, M2)

def common_prefix_length(String1, String2):
    Chars1 = list(String1)
    Chars2 = list(String2)
    return common_prefix_length_helper(Chars1, Chars2, 0)

def common_prefix_length_helper(Chars1, Chars2, Length):
    if not Chars1 or not Chars2:
        return Length
    elif Chars1[0] != Chars2[0]:
        return Length
    else:
        return common_prefix_length_helper(Chars1[1:], Chars2[1:], Length + 1)

def to_upper_case(strings):
    return [s.upper() for s in strings]

def process_line(line):
    if line == "":
        print()
    else:
        Day_names = line.split()
        Upper = to_upper_case(Day_names)
        Length = minimum_abbreviation_length(Upper, 0)
        print(f'{Length} {line}')

def process_file(file):
    with open(file, 'r') as f:
        for line in f:
            process_line(line)

def main():
    process_file("days_of_week.txt")

main()
```