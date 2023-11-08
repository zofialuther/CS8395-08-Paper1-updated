def is_perfect_number(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num

def generate_list(m, n):
    return list(range(m, n+1))

def main():
    numbers = generate_list(1, 10000)
    perfect_numbers = [num for num in numbers if is_perfect_number(num)]
    print(perfect_numbers)

main()