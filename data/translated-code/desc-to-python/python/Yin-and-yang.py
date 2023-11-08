symbol = []

for i in range(20):
    symbol.append([' '] * 20)

for i in range(10):
    for j in range(20):
        if (i - 10) ** 2 + (j - 5) ** 2 <= 100:
            symbol[i][j] = '@'
        if (i - 10) ** 2 + (j - 15) ** 2 <= 100:
            symbol[i][j] = ' '

for i in range(10, 20):
    for j in range(20):
        if (i - 10) ** 2 + (j - 5) ** 2 <= 100:
            symbol[i][j] = ' '
        if (i - 10) ** 2 + (j - 15) ** 2 <= 100:
            symbol[i][j] = '@'

result = '\n'.join([''.join(row) for row in symbol])
print(result)