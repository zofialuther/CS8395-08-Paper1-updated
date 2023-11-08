def show_proper_divisors_of_range(start, end):
    for i in range(start, end+1):
        divisor_list = []
        for j in range(1, i):
            if i % j == 0:
                divisor_list.append(j)
        print(str(i) + ":" + str(divisor_list))

def find_most_proper_divisors_in_range(start, end):
    max_divisors = 0
    max_num = 0
    for i in range(start, end+1):
        divisor_count = 0
        for j in range(1, i):
            if i % j == 0:
                divisor_count += 1
        if divisor_count > max_divisors:
            max_divisors = divisor_count
            max_num = i
    result = "num(" + str(max_num) + ")-divisor_count(" + str(max_divisors) + ")"
    return result