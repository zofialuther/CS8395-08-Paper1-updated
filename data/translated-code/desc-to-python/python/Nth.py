def ord(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix

for i in range(0, 26):
    print(ord(i))

for i in range(250, 266):
    print(ord(i))

for i in range(1000, 1026):
    print(ord(i))