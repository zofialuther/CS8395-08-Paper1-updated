for i in range(1, 13):
    print('\t', i, end='')
print('\n-----------------------------------------')
for i in range(1, 13):
    print(i, '|', end='')
    for j in range(1, 13):
        print('\t', i*j, end='')
    print('\n')