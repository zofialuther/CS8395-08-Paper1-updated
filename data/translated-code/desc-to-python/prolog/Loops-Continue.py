def print_list(min_value, max_value):
    if min_value <= max_value:
        print(min_value)
        if min_value % 5 == 0:
            print()
        print_list(min_value + 1, max_value)

print_list(1, 10)