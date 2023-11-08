def remove_duplicates(arr):
    unique_values = []
    for num in arr:
        if num not in unique_values:
            unique_values.append(num)
    return unique_values