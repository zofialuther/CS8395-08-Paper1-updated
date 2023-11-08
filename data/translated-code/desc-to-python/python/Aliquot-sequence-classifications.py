def sum_of_divisors(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

def aliquot_sequence_type(num_range):
    for num in num_range:
        sequence = [num]
        current_num = num
        while True:
            next_num = sum_of_divisors(current_num)
            if next_num in sequence:
                if next_num == num:
                    if len(sequence) == 1:
                        print(f"{num} is a prime number")
                    else:
                        print(f"{num} is a perfect number")
                else:
                    print(f"{num} is an amicable number")
                break
            elif next_num == 1:
                if len(sequence) == 1:
                    print(f"{num} is an aspiring number")
                else:
                    print(f"{num} is a non-terminating number")
                break
            elif next_num == num:
                print(f"{num} is a cyclic number")
                break
            elif next_num in sequence:
                print(f"{num} is a sociable number")
                break
            sequence.append(next_num)
            current_num = next_num

aliquot_sequence_type(range(1, 101))