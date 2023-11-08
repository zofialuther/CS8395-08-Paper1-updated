n = 5
array = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    array[i][i] = 1

for row in array:
    print(row)