def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes

def group_primes(primes):
    groups = {}
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            diff = primes[j] - primes[i]
            if diff not in groups:
                groups[diff] = [primes[i]]
            groups[diff].append(primes[j])
    return groups

def show_group(groups, group_type):
    if group_type in groups:
        group = groups[group_type]
        print(f"Group {group_type}: Length - {len(group)}, First - {group[0]}, Last - {group[-1]}")

primes = generate_primes(1000000)
groups = group_primes(primes)

show_group(groups, 2)
show_group(groups, 4)
show_group(groups, 6)