def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))
    return n == 1

def get_next_number(n):
    n += 1
    while not is_happy(n):
        n += 1
    return n

def process_digits(n):
    return [int(i) for i in str(n)]

def happy_numbers(Nb):
    numbers = []
    current_number = 1
    for _ in range(Nb):
        numbers.append(current_number)
        current_number = get_next_number(current_number)
    return numbers