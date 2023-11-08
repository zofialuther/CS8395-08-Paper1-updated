# Python equivalent of the given Java code

def display_map(map):
    for key in range(1, 10):
        print(f"{key} : {map[key]}")


def get_palindromic_gapful_ending(count_returned, first_how_many):
    map = {i: [] for i in range(1, 10)}
    map_count = {i: 0 for i in range(1, 10)}
    not_populated = True
    n = 101
    while not_populated:
        if is_gapful(n):
            index = int(n % 10)
            if map_count[index] < first_how_many:
                map[index].append(n)
                map_count[index] += 1
                if len(map[index]) > count_returned:
                    map[index].pop(0)
            finished = all(map_count[i] >= first_how_many for i in range(1, 10))
            if finished:
                not_populated = False
        n = next_palindrome(n)
    return map


def is_gapful(n):
    s = str(n)
    return n % int(s[0] + s[-1]) == 0


def length(n):
    return len(str(n))


def next_palindrome(n):
    length = length(n)
    if length % 2 == 0:
        length //= 2
        n = int(n / 10**length)
        n += 1
        if power_ten(n):
            return int(str(n) + reverse(int(n / 10)))
        return int(str(n) + reverse(n))
    length = (length - 1) // 2
    n = int(n / 10**length)
    n += 1
    if power_ten(n):
        return int(str(n) + reverse(int(n / 100)))
    return int(str(n) + reverse(int(n / 10)))


def power_ten(n):
    while n > 9 and n % 10 == 0:
        n //= 10
    return n == 1


def reverse(n):
    return int(str(n)[::-1])


if __name__ == "__main__":
    print("First 20 palindromic gapful numbers ending in:")
    display_map(get_palindromic_gapful_ending(20, 20))

    print("\nLast 15 of first 100 palindromic gapful numbers ending in:")
    display_map(get_palindromic_gapful_ending(15, 100))

    print("\nLast 10 of first 1000 palindromic gapful numbers ending in:")
    display_map(get_palindromic_gapful_ending(10, 1000))