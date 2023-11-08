def powersetlist(input_list):
    result = [[]]
    for i in input_list:
        result += [subset + [i] for subset in result]
    return result

sample_list = [0, 1, 2, 3]
print(powersetlist(sample_list))