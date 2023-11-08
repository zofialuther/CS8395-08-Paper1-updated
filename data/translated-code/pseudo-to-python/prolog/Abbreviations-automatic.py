def minimum_abbreviation_length(Day_names, Min_length):
    Sorted_names = sorted(Day_names)
    return minimum_abbreviation_length_recursive(Sorted_names, Min_length, 1)

def minimum_abbreviation_length_recursive(names, min_length, m1):
    if len(names) == 1:
        return min_length
    else:
        name1 = names[0]
        name2 = names[1]
        length = common_prefix_length(name1, name2)
        m2 = max(m1, length + 1)
        return minimum_abbreviation_length_recursive(names[1:], min_length, m2)

def common_prefix_length(string1, string2):
    chars1 = list(string1)
    chars2 = list(string2)
    return common_prefix_length_recursive(chars1, chars2, 0)

def common_prefix_length_recursive(chars1, chars2, length):
    if not chars1 or not chars2:
        return length
    else:
        c1 = chars1[0]
        c2 = chars2[0]
        if c1 != c2:
            return length
        else:
            return common_prefix_length_recursive(chars1[1:], chars2[1:], length + 1)

def to_upper_case(strings):
    upper_case = [string.upper() for string in strings]
    return upper_case

def process_line(line):
    if not line:
        print()
        return
    else:
        day_names = line.split()
        upper = to_upper_case(day_names)
        length = minimum_abbreviation_length(upper, 0)
        print(f'{length} {line}')

def process_stream(stream):
    string = input()
    if string != "end_of_file":
        process_line(string)
        process_stream(stream)
    else:
        return

def process_file(file):
    with open(file, "r") as f:
        process_stream(f)

def main():
    process_file("days_of_week.txt")

main()