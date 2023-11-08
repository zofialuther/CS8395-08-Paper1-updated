def spellOrdinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

def main():
    numbers = [1, 2, 3, 4, 5, 11, 65, 100, 101, 272, 23456, 8007006005004003]
    for n in numbers:
        print(str(n) + "\t" + spellOrdinal(n))