def calculate_median(input_list):
    if len(input_list) == 0:
        return 0
    else:
        sorted_list = sorted(input_list)
        if len(sorted_list) % 2 == 0:
            middle_index = len(sorted_list) // 2
            median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
        else:
            middle_index = len(sorted_list) // 2
            median = sorted_list[middle_index]
        return median