```python
def small_name(number, name, ordinal):
    return (number, name, ordinal)

def big_names():
    return [
        (100, 'hundred', 'hundredth'),
        (1000, 'thousand', 'thousandth'),
        (1000000, 'million', 'millionth'),
        (1000000000, 'billion', 'billionth'),
        (1000000000000, 'trillion', 'trillionth'),
        (1000000000000000, 'quadrillion', 'quadrillionth'),
        (1000000000000000000, 'quintillion', 'quintillionth'),
        (1000000000000000000000, 'sextillion', 'sextillionth'),
        (1000000000000000000000000, 'septillion', 'septillionth')
    ]

def big_name(number, big_names):
    for i in range(len(big_names)):
        if number < big_names[i][0]:
            return big_names[i][1]

def get_big_name(big, cardinal_ordinal):
    if cardinal_ordinal == 'cardinal':
        return big[1]
    else:
        return big[2]

def get_small_name(number, cardinal_ordinal):
    if cardinal_ordinal == 'cardinal':
        for i in range(len(small_names)):
            if small_names[i][0] == number:
                return small_names[i][1]
    else:
        for i in range(len(small_names)):
            if small_names[i][0] == number:
                return small_names[i][2]

def number_name(number, type, small_names, big_names):
    if number < 20:
        return get_small_name(number, type)
    elif number < 100:
        n = number % 10
        if n == 0:
            return get_small_name(number, type)
        else:
            n1 = number - n
            name1 = get_small_name(n1, 'cardinal')
            name2 = get_small_name(n, type)
            return f"{name1}-{name2}"
    else:
        b = big_name(number, big_names)
        n = number // b[0]
        name1 = number_name(n, 'cardinal', small_names, big_names)
        m = number % b[0]
        if m == 0:
            name2 = get_big_name(b, type)
        else:
            name3 = number_name(m, type, small_names, big_names)
            name2 = f"{b[1]} {name3}"
        return f"{name1} {name2}"
```