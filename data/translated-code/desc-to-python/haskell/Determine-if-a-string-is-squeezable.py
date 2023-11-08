def collapse_string(list_of_tuples):
    for string, char in list_of_tuples:
        collapsed_string = ''
        prev_char = ''
        for s in string:
            if s != char or s != prev_char:
                collapsed_string += s
            prev_char = s
        print(f"Original string: {string}, Collapsed string: {collapsed_string}, Collapsed character: {char}")