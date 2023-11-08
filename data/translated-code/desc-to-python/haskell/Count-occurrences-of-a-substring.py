def count(first_list, second_list):
    occurrences = []
    for i in range(len(second_list) - len(first_list) + 1):
        if second_list[i:i + len(first_list)] == first_list:
            occurrences.append(i)
    return len(occurrences)