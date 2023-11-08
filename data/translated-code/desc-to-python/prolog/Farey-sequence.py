def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def farey_sequence(n):
    farey = [(0, 1), (1, 1)]
    for den in range(2, n+1):
        for num in range(1, den):
            if gcd(num, den) == 1:
                farey.append((num, den))
    return farey

def print_farey_sequence(sequence):
    for num, den in sequence:
        print(f"{num}/{den}")

def compare_rational_numbers(r1, r2):
    return r1[0] * r2[1] - r1[1] * r2[0]

# Task 1
farey_11 = farey_sequence(11)
print_farey_sequence(farey_11)

# Task 2
farey_1000 = farey_sequence(1000)
print(len(farey_1000))