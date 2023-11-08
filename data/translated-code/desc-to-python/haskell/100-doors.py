def find_odd_indices(n):
    zero_list = [0] * n
    toggle_list = []
    for i in range(n):
        if i % 2 == 0:
            toggle_list.append(zero_list[i] + 1)
        else:
            toggle_list.append(zero_list[i] + 0)
    odd_indices = [i for i, num in enumerate(toggle_list) if num % 2 != 0]
    return odd_indices