```python
def divisor(num, div):
    return num % div == 0

def proper_divisor(num, div):
    return num % div == 0 and num != div

def assoc_num_divsSum_in_range(start, end):
    result = {}
    for i in range(start, end+1):
        divisors = [j for j in range(1, i) if divisor(i, j)]
        result[i] = sum(divisors)
    return result

def get_amicable_pair(num, assoc_list):
    pair = (num, assoc_list[num])
    if pair[1] in assoc_list and assoc_list[pair[1]] == num and pair[0] != pair[1]:
        return pair
    else:
        return None

def amicable_pairs_under_20000(end):
    result = []
    assoc_list = assoc_num_divsSum_in_range(1, end)
    for num in range(1, end+1):
        pair = get_amicable_pair(num, assoc_list)
        if pair:
            result.append(pair)
    return result
```