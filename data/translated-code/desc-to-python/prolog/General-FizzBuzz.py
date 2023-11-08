def factor_strings(input_list):
    result = []
    for num, string in input_list:
        factors = [i for i in range(1, num+1) if num % i == 0]
        result.append((num, factors, string))
    return result