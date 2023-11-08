numbers = [1, 2, 3, 4, 5, 10, 11, 12, 13]

def spellOrdinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

mapM_(lambda x: print(f"{x} {spellOrdinal(x)}"), numbers)